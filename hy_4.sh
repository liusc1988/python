cd /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4
makeblastdb -in /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/RF/hongyang_v3/Hongyang_cds_v3.0.fa -input_type fasta -dbtype nucl -title hy -parse_seqids -out /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4/MCScanX/hy -logfile cds.log
pkurun-cnlong 1 20 'blastn -query /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/customer_backup_Y543/05.Annotation/02.gene_prediction/Chr_genome_final_gene.gff3.cds -db /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4/MCScanX/hy -out hy_4.blast -evalue 1e-10 -num_threads 20 -outfmt 6 -num_alignments 5'
python -m jcvi.formats.gff bed --type=mRNA --key=ID /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/RF/hongyang_v3/Hongyang_v3.0_update.gff3  -o hy.bed
awk '{print $1"\t"$4"\t"$2"\t"$3}' hy.bed > hy.gff
/gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/result/4cds.gff
perl -0076 -ane '@F=map{s/[>\r\n]//gr}@F;$id=shift @F;print $id,qq{\t},length (join q{},@F),qq{\n} if $id'  /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/RF/hongyang_v3/Hongyang_genome_v3.0_update.fa > hy.chr.length
cat /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/result/4cds.gff hy.gff > hy_4.gff
/gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/MCScanX/MCScanX hy_4 -s 30 -b 2
java circle_plotter -g /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4/MCScanX/hy_4.gff -s /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4/MCScanX/hy_4.collinearity -c /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4/MCScanX/circle2.ctl -o /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4/MCScanX/hy_4.circle.PNG
pkurun-cnlong 1 20 'orthofinder -f orthofinder -S diamond -t 20 -a 20 -d -M msa -T iqtree'
setwd("/gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4/orthofinder/OrthoFinder/Results_Mar19_1/Species_Tree")
library('ggtree')
library('treeio')
tree <- read.tree('SpeciesTree_rooted.txt')
tree$tip.lable<- gsub('_repr','',tree$tip.label)

tree$tip.lable<- gsub('(^[A-Z])','\\l.',tree$tip.label)
pdf("SpeciesTree_rooted.pdf",family="GB1")
ggplot(tree,aes(x,y)) + geom_tree() + theme_tree() + geom_tiplab(size=3)
dev.off()
/gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4/orthofinder/OrthoFinder/Results_Mar19_1/Gene_Trees/OG0000000_tree.txt
tree <- read.tree('/gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/hy_4/orthofinder/OrthoFinder/Results_Mar19_1/Gene_Trees/OG0000000_tree.txt')
tree$tip.lable<- gsub('_repr','',tree$tip.label)

tree$tip.lable<- gsub('(^[A-Z])','\\l.',tree$tip.label)
pdf("OG0000000_tree.pdf",family="GB1")
ggplot(tree,aes(x,y)) + geom_tree() + theme_tree() + geom_tiplab(size=3)
dev.off()