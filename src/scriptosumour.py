import numpy as np
from itertools import izip
ff=open("base_model2.tsv")
mm={}
for i in ff:
    g=i[:-1].split("\t")
    mm[g[0]]=map(float,g[1:])
f=open("triseg.txt")
ll=[]
for i in f:
    gg=i[:-2].split("\t")
    l=[]
    for j in gg[:-1]:
        l.append(mm[j])
    else:
        l.append([0.0]*100)
    ll.append(np.sum(l,axis=0))
summed=[]
for r,g,b in izip(*[iter(ll)]*3):
    summed.append(np.sum([r,g,b],axis=0))
for i in summed:
    k=i.tolist()
    for j in range(len(k)):
        print k[j],"\t",
    print "\n",
