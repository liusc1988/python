import sys
import re
i = sys.argv[1]
o = sys.argv[2]
o1 = sys.argv[3]
#python vcf_stat.py fam-denovo.vcf fam-filter.vcf stat.table
with open(o,'a') as w1:
 def d(inn):
#0/1:19,1:20:1:1,0,658
  f = inn.split(":")
  if not re.match( r'\.', f[0]):
    f1=f[1].split(",")
    g=['0/0:23,0:23:0:.:.:0,0,124',0,0,0]
    if re.match( r'0/1', f[0]) or re.match( r'0\|1', f[0]) :
        #print (f[0])
        if int(f1[1])<4:
            g[0]=r'0/0:23,0:23:0:.:.:0,0,124'
            g[1]=0
            g[2]=0
        else:
            #print(f1[1])
            g[0]=inn
            g[1]=1
            g[2]=float(f1[1])/float(f1[1]+f1[0])
    elif re.match(r'1', f[0]):
        if int(f1[1]) < 4:
            g[0] = r'./.:0,0:0:.:0,0,0'
            g[1] = 0
            g[2]=0
        else:
            g[0]=inn
            g[1]=0.1
            g[2]=0
    else:
            g[0]=r'./.:0,0:0:.:0,0,0'
            g[1]=0
            g[2]=0
    #print(f)
    if int(f[2])<10:
        g[3]=0
        g[0] = r'./.:0,0:0:.:0,0,0'
        g[1] = 0
        g[2] = 0
    else:
        g[3]=1
    #print(g)
  else:
     g = ['./.:0,0:23:0:.:.:0,0,124', 0, 0, 0]

  return g

 a={}
 with open(i) as f:
    for line in f:
        l=line.rstrip()
        if not re.search( r'Cla97Scf', l) and re.match( r'#', l):
            w1.write(l+"\n")
        elif re.match(r'Cla97Chr', l):
            x = l.split("\t")
            if re.match( r'PASS', x[6]):
                if not re.search( ',', x[4]):
                    c=0
                    for i1 in range(9, len(x)):
                        #print(i1)
                        h = list()
                        h= d (x[i1])

                        x[i1]=h[0]
                        #print (h[2])
                        if h[3]>0 and h[1]==1:
                            #print (h)
                            c += h[1]
                            y=x[3]+"_"+x[4]
                            if y in a.keys():
                                if i1 in a[y].keys():

                                    a[y][i1] += 1

                                else:
                                    a[y].setdefault(i1, 1)
                                    #a[y]={i1:1}

                            else:
                                a[y]={}
                        else:
                            c += h[1]
                            y = x[3] + "_" + x[4]
                            if y in a.keys():
                                y = x[3] + "_" + x[4]
                                if i1 in a[y].keys():
                                    a[y][i1] += 0
                                else:
                                    a[y].setdefault(i1, 0)
                            else:
                                a[y]={}
                    if c>0.9:w1.write('\t'.join(x)+"\n")
with open(o1, 'a') as w2:
    for i in a.keys():
        b=i
        for i1 in a[i].keys():
            b=b+"\t"+str(a[i][i1])
            print(i+str(i1)+str(a[i][i1]))
        b=b+'\n'
        w2.write(b)
