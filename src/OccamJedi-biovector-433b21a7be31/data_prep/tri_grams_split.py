# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:27:10 2016

@author: mohnish
"""

from nltk import ngrams
data_file = "../data/sequences.txt"
dest_file = "../data/trinewseq1.txt"
with open(data_file) as f:
    raw_sequences = f.readlines()
    
for seq in raw_sequences:
    tri_grams = ngrams(seq[:-1],3)
    tri_grams = list(tri_grams)
    with open(dest_file,"a") as f:
        for i in range(0,len(tri_grams),3):
            print(tri_grams[i])
            f.write(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2]+"\t")
        f.write("\n")
        for i in range(1,len(tri_grams),3):
            f.write(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2]+"\t")
        f.write("\n")
        for i in range(2,len(tri_grams),3):
            f.write(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2]+"\t")
        f.write("\n")
