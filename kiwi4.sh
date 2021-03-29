conda activate r40
cd /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/result
makeblastdb -in /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/customer_backup_Y543/05.Annotation/02.gene_prediction/Chr_genome_final_gene.gff3.cds -input_type fasta -dbtype nucl -title cds -parse_seqids -out /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/db/cds -logfile cds.log
pkurun-cnlong 1 20 'blastn -query /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/customer_backup_Y543/05.Annotation/02.gene_prediction/Chr_genome_final_gene.gff3.cds -db /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/db/cds -out 4cds.blast -evalue 1e-10 -num_threads 20 -outfmt 6 -num_alignments 5'
python -m jcvi.formats.gff bed --type=mRNA --key=ID /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/customer_backup_Y543/05.Annotation/02.gene_prediction/Chr_genome_final_gene.gff3 -o 4cds.bed
awk '{print $1"\t"$4"\t"$2"\t"$3}' 4cds.bed > 4cds.gff
/gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/MCScanX/MCScanX 4cds -s 30
cd /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/MCScanX/downstream_analyses
java circle_plotter -g /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/result/4cds.gff -s /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/result/4cds.collinearity -c /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/MCScanX/downstream_analyses/circle.ctl -o /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/result/4cds.circle.PNG
java /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/MCScanX/downstream_analyses/circle_plotter -g /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/result/4cds.gff -s /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/result/4cds.collinearity -c /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/MCScanX/downstream_analyses/circle2.ctl -o /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/result/4cds.1.2.circle.PNG