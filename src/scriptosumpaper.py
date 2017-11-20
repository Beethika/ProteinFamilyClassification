import numpy as np
from itertools import izip
ff=open("protvecpaper.txt")
mm={}
for i in ff:
    g=i[:-1].split("\t")
    mm[g[0]]=map(float,g[1:])
f=open("trinewseq.txt")
ll=[]
seq_count =0
for i in f:
    if seq_count not in [(157730*3)-1,(157730*3)-2,157730*3,(320296*3)-1,(320296*3)-2,320296*3,(321547*3)-1,(321547*3)-2,321547*3,(156442*3)-1,(156442*3)-2,156442*3,(156443*3)-1,(156443*3)-2,156443*3,(195552*3)-2,(195552*3)-1,195552*3,(269564*3)-2,(269564*3)-1,269564*3]:
        gg=i[:-2].split("\t")
        l=[]
        for j in gg:
            l.append(mm[j])
        ll.append(np.sum(l,axis=0))
    seq_count +=1
print len(ll)
summed=[]
for r,g,b in izip(*[iter(ll)]*3):
    summed.append(np.sum([r,g,b],axis=0))
for i in summed:
    print i,"\t",
