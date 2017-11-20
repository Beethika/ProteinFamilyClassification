import numpy as np
from itertools import izip
ff=open("base_model3.tsv")
mm={}
for i in ff:
    g=i[:-1].split("\t")
    mm[g[0]]=map(float,g[1:])
f=open("segwithtrigram.txt")
ll=[]
for i in f:
    gg=i[:-1].split("\t")
    l=[]
    for j in gg:
        if len(j) > 1:
            l.append(mm[j])
        else:
            l.append([0.0]*100)
    ll.append(np.sum(l,axis=0))
for i in ll:
    k=i.tolist()
    for j in range(len(k)):
        print k[j],"\t",
    print "\n",

