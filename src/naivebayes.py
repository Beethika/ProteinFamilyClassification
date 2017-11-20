from __future__ import division
from sklearn.naive_bayes import MultinomialNB
from sklearn import cross_validation
import numpy as np
import glob
import sklearn
from sklearn import svm
import numpy as np
import glob
from nltk import ngrams
from random import randint
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
from collections import Counter
def compute_measures(tp, fp, fn, tn):
     """Computes effectiveness measures given a confusion matrix."""
     specificity = tn / (tn + fp)
     sensitivity = tp / (tp + fn)
     return sensitivity, specificity
def accuracy(labelcorrect,labelpred):
    return round(sklearn.metrics.accuracy_score(labelcorrect, labelpred),2)

def bayesscore(positive_sequences,negative_sequences,testsequences):
	listoftrigrams1=[]  
	for seq in positive_sequences:
	    tri_grams = ngrams(seq[0],3)
	    tri_grams = list(tri_grams)
	    for i in range(0,len(tri_grams),3):
		#print(tri_grams[i])
		listoftrigrams1.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
	    for i in range(1,len(tri_grams),3):
		listoftrigrams1.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
	    for i in range(2,len(tri_grams),3):
		listoftrigrams1.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
	positiveseqcount=Counter(listoftrigrams1)

	listoftrigrams=[]  
	for seq in negative_sequences:
	    tri_grams = ngrams(seq[0],3)
	    tri_grams = list(tri_grams)
	    for i in range(0,len(tri_grams),3):
		#print(tri_grams[i])
		listoftrigrams.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
	    for i in range(1,len(tri_grams),3):
		listoftrigrams.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
	    for i in range(2,len(tri_grams),3):
		listoftrigrams.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
	negativeseqcount=Counter(listoftrigrams)
	##Likelihood computation
	uniquetrigrams=list(set(positiveseqcount.keys()+negativeseqcount.keys()))
	ps_likelihood={}
	neg_likelihood={}
	for i in uniquetrigrams:
	    ps_likelihood[i]=(1+positiveseqcount[i])/(len(uniquetrigrams)+len(listoftrigrams1))
	    neg_likelihood[i]=(1+negativeseqcount[i])/(len(uniquetrigrams)+len(listoftrigrams))
	predictedlabels=[]
	for testsequence in testsequences:
	    overlappingtrigramsps=[]
	    overlappingtrigramsns=[]
	    sample_seq=ngrams(testsequence[0],3)
	    tri_grams = list(sample_seq)
	    for i in range(0,len(tri_grams),3):
	        #print(tri_grams[i])
	        overlappingtrigramsps.append(ps_likelihood.get(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2],0))
	        overlappingtrigramsns.append(neg_likelihood.get(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2],0))
	    for i in range(1,len(tri_grams),3):
	        overlappingtrigramsps.append(ps_likelihood.get(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2],0))
	        overlappingtrigramsns.append(neg_likelihood.get(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2],0))
	    for i in range(2,len(tri_grams),3):
	        overlappingtrigramsps.append(ps_likelihood.get(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2],0))
	        overlappingtrigramsns.append(neg_likelihood.get(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2],0))
	    pos_score= np.sum(np.array(overlappingtrigramsps))
	    neg_score= np.sum(np.array(overlappingtrigramsns))
	    print pos_score,neg_score
	    if pos_score > neg_score:
	        predictedlabels.append(1)
	    else:
	        predictedlabels.append(0)
	return predictedlabels

def bayesmultinomialcrossvalidation(modxtr,modytr):
    ##10-fold test for mod xtr
    modxtr=np.array(modxtr)
    modytr=np.array(modytr)
    results = []
    results1 = []
    results2 = []
    cv1 = cross_validation.StratifiedKFold(modytr, n_folds=10)
    for traincv, testcv in cv1:
        posseq=[]
        negseq=[]
	labelist=modytr[traincv].tolist()
	seqlist=modxtr[traincv].tolist()
        for i in range(len(labelist)):
	    #print i
            if labelist[i] == 1:
                posseq.append(seqlist[i])
            else:
                negseq.append(seqlist[i])   
        probas = bayesscore(posseq, negseq,modxtr[testcv].tolist())
        #evaluate_cluster(modytr[testcv],probas,"10-fold")
        truen, falsep, falsen, truep = confusion_matrix(modytr[testcv], np.array(probas)).ravel()
        print truen, falsep, falsen, truep
        sens,speci=compute_measures(truep, falsep, falsen, truen)
        results.append(accuracy(modytr[testcv],probas))
        results1.append(sens)
        results2.append(speci)
    print "Mean accuracy: " + str( np.array(results).mean())
    print "Mean specificity: " + str( np.array(results1).mean())
    print "Mean sensitivity: " + str( np.array(results2).mean())


listoffamilies=glob.glob('familiessequences/*.txt')
print len(listoffamilies)
listoffamilies.remove('familiessequences/"7tm_1".txt')
newfile=open('familiessequences/"7tm_1".txt')
positive_sequences=[]
positive_labels=[]
for ii in newfile:
    positive_sequences.append(ii[:-2].split("\t"))
    positive_labels.append(1)
print len(positive_sequences)    
x=[randint(0,len(listoffamilies)-1) for p in range(0,len(positive_sequences))]
print len(x)
negative_sequences=[]
negative_labels=[]
for i in x:
    f=open(listoffamilies[i])
    seq=[]
    for j in f:
        seq.append(j[:-2].split("\t"))
    y=randint(0,len(seq)-1)
    #print y
    negative_sequences.append(seq[y])
    negative_labels.append(0)
posnegrep=positive_sequences+negative_sequences
posneglabels=positive_labels+negative_labels

bayesmultinomialcrossvalidation(posnegrep,posneglabels)


