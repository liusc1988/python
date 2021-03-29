import sys
import re
i = sys.argv[1]
i1 = sys.argv[2]

#python sub_cds.py /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/customer_backup_Y543/05.Annotation/02.gene_prediction/Chr_genome_final_gene.gff3 /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/customer_backup_Y543/05.Annotation/02.gene_prediction/Chr_genome_final_gene.gff3.cds
with open(o,'a') as w1:
with open(i) as f:
    for line in f:
        l = line.rstrip()
        x = l.split("\t")
        if x[2]=="gene":
            m = re.match(r'ID=(.*) ', x[8])
            a[m.group(1)]=x[0]
with open(i1) as f:
    n=0
    o=0
    for line in f:
        l=line.rstrip()
        m=re.match( r'>(.*)gene=(.*)', l)
        if re.match( r'>(.*)gene=(.*)', l):
            if re.match( r'Chr01',a[m.group(2)]):
                o=a[m.group(2)]+".fa"
                with open(o, 'a') as w1:
                    w1.write(l + "\n")
                n=1
            else:
                n=0
        elif n==1:
            with open(o, 'a') as w1:
                w1.write(l + "\n")
#>Achi01G000180.1 gene=Achi01G000180
#Chr01C  EVM     gene    1076    18874   .       +       .       ID=Achi01G000010