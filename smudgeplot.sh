
jellyfish count -C -m 21 -s 1000000000 -t 20 /gpfs1/deng_pkuhpc/deng_test/PJ/kiwi/poly4ass/customer_backup_Y543/01.Raw_data/Survey/*.fq.gz -o kmer_counts.jf
jellyfish histo kmer_counts.jf > kmer_k21.hist
L=$(smudgeplot.py cutoff kmer_k21.hist L)
U=$(smudgeplot.py cutoff kmer_k21.hist U)
echo $L $U # these need to be sane values like 30 800 or so
jellyfish dump -c -L $L -U $U kmer_counts.jf | smudgeplot.py hetkmers -o kmer_pairs
smudgeplot.py plot kmer_pairs_coverages_2.tsv -o my_genome
