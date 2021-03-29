INDEX=/lustre1/deng_pkuhpc/deng_test/rf/97103_genome_v2/97103_genome_v2
PICARD=/lustre1/deng_pkuhpc/deng_test/SF/min3/share/picard-2.22.4-0/picard.jar
CLEANDATA=/lustre1/deng_pkuhpc/liusc/X101SC20090776/2.cleandata
TEMP=/lustre1/deng_pkuhpc/deng_test/projects/kiwi/tmp
INDEL=/lustre1/deng_pkuhpc/deng_test/projects/watermelon/pub/cucurbit/reseq/watermelon/v2/1_indel.vcf
SNP=/lustre1/deng_pkuhpc/deng_test/projects/watermelon/pub/cucurbit/reseq/watermelon/v2/1_SNP.vcf
rule all:
    input:
        expand()
        "plots/quals.svg"
rule f_bam
    input:
        q1={CLEANDATA}/{sample}_{id}/{sample}_{id}_1.clean.fq.gz
		q2={CLEANDATA}/{sample}_{id}/{sample}_{id}_2.clean.fq.gz
    output:
        "mapped_reads/{sample}.bam"
    threads: 20
    params:
        rg=r"@RG\tID:{sample}\tSM:{sample}"
    shell:
        bwa mem -v 2  -M -R '{params.rg}' -t {threads} INDEX $q1 $q2|samtools view -Sb - > {output}
rule bam_sort
    input:
        rules.f_bam.output
    output:
        "mapped_reads/{sample}.sort.bam"
    threads: 20
    params:

    shell:
        java -Xmx60g -Djava.io.tmpdir= {TEMP} -jar {PICARD} SortSam INPUT={input} OUTPUT={output} SORT_ORDER=coordinate
rule samtools_index:
    input:
        "mapped_reads/{sample}.sort.bam"
    output:
        "mapped_reads/{sample}.sort.rmdup.bam"
    shell:
        "java -Xmx60g -Djava.io.tmpdir={TEMP} -jar {PICARD} MarkDuplicates REMOVE_DUPLICATES=true I={input} O={output} M=mapped_reads/{sample}.txt"
rule samtools_index:
    input:
        rules.bam_sort.output
    output:
        "mapped_reads/{sample}.sort.bam.bai"
    shell:
        "samtools index {input}"
rule BaseRecal:
    input:
        rules.bam_sort.output
    output:
        "mapped_reads/{sample}.table"
    shell:
        "gatk --java-options '-Xmx60g -Djava.io.tmpdir={TEMP}' BaseRecalibrator -R {REF} -I {input} --known-sites {SNP} --known-sites {INDEL} -O {output}\n"
rule ApplyBQSR:
    input:
        rules.BaseRecal.output
        "mapped_reads/{sample}.sort.bam"
    output:
        "mapped_reads/{sample}.BQSR.bam"
    shell:
        "gatk --java-options '-Xmx60g -Djava.io.tmpdir={TEMP}' ApplyBQSR --bqsr-recal-file {input[0]} -R {REF} -I {input[1]} -O {output}
rule HaplotypeCaller:
    input:
        "mapped_reads/{sample}.BQSR.bam"
    output:
        "gvcf/{sample}.gvcf"
    threads: 20
    shell:
        "gatk --java-options '-Xmx60g -Djava.io.tmpdir={TEMP}' HaplotypeCaller -R {REF} --native-pair-hmm-threads {threads} -I {input} -ERC GVCF -O {output}
rule HaplotypeCaller:
    input:
        "mapped_reads/{sample}.BQSR.bam"
    output:
        "gvcf/{sample}.gvcf"
    threads: 20
    shell:
        "gatk --java-options '-Xmx60g -Djava.io.tmpdir={TEMP}' HaplotypeCaller -R {REF} --native-pair-hmm-threads {threads} -I {input} -ERC GVCF -O {output}
