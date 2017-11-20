# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:29:47 2016

@author: mohnish
"""
#https://radimrehurek.com/gensim/models/word2vec.html
#Documentation here

import logging
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

data_file = "../data/allsegtraincmplete.txt"
model_name = "base_model2"
dest_rep = "../data/vectors/"+model_name+".tsv"


#with open(data_file) as f:
#    raw_sequences = f.readlines()

#sequences = []    
#for sentence in raw_sequences:
#    new = []
#    new = sentence[:-1].split(" ")
#    sequences.append(new)

#To stream a large data corpus
s = LineSentence(data_file)

#Training model
model = Word2Vec(s, size=100, window=25, min_count=1, workers=1)
model.save("../data/models/"+model_name)

with open(dest_rep,'w') as f:
    for word, obj in model.vocab.items():
        f.write(word)
        for i in model[word]:
            f.write("\t"+str(i))
        f.write("\n")
