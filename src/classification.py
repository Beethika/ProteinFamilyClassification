from __future__ import division
import sklearn
from sklearn import svm
import numpy as np
import glob
from random import randint
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
def compute_measures(tp, fp, fn, tn):
     """Computes effectiveness measures given a confusion matrix."""
     specificity = tn / (tn + fp)
     sensitivity = tp / (tp + fn)
     return sensitivity, specificity
def accuracy(labelcorrect,labelpred):
    return round(sklearn.metrics.accuracy_score(labelcorrect, labelpred),2)
def mutualinfo(labelcorrect,labelpred):
    return round(sklearn.metrics.mutual_info_score(labelcorrect, labelpred,   contingency=None),2)
def normmutualinfo(labelcorrect,labelpred):
    return round(sklearn.metrics.normalized_mutual_info_score(labelcorrect, labelpred),2)
def fbeta(labelcorrect,labelpred):
    return round(sklearn.metrics.fbeta_score(labelcorrect, labelpred, beta=0.5, labels=None, pos_label=1, average='micro'),2)
def rand(labelcorrect,labelpred):
    return round(sklearn.metrics.adjusted_rand_score(labelcorrect,labelpred),2)
def precision(labelcorrect,labelpred):
    return round(sklearn.metrics.precision_score(labelcorrect,labelpred),2) 
def svmcrossvalidation(modxtr,modytr):
    ##10-fold test for mod xtr
    modxtr=np.array(modxtr)
    modytr=np.array(modytr)
    C_2d_range = [1e-5,1e-4,1e-3,1e-2,1e-1,0]
    gamma_2d_range = [1e-5,1e-4,1e-3,1e-2,1e-1,0]
    classifiers = []
    for C in C_2d_range:
        for gamma in gamma_2d_range:
            print C,gamma
            results = []
            results1 = []
            results2 = []
            clf =svm.SVC(C=C, gamma=gamma,kernel='rbf')
            classifiers.append((C, gamma, clf))
    #clf1 = svm.SVC()
            cv1 = cross_validation.StratifiedKFold(modytr, n_folds=10)
            for traincv, testcv in cv1:
                probas = clf.fit(modxtr[traincv], modytr[traincv]).predict(modxtr[testcv])
                #evaluate_cluster(modytr[testcv],probas,"10-fold")
                truen, falsep, falsen, truep = confusion_matrix(modytr[testcv], probas).ravel()
                print truen, falsep, falsen, truep
                sens,speci=compute_measures(truep, falsep, falsen, truen)
                results.append(accuracy(modytr[testcv],probas))
                results1.append(sens)
                results2.append(speci)
            print "Mean accuracy: " + str( np.array(results).mean() )
            print "Mean specificity: " + str( np.array(results1).mean() )
            print "Mean sensitivity: " + str( np.array(results2).mean() )
listoffamilies=glob.glob('familiesword2vec/*.tri')
print len(listoffamilies)
listoffamilies.remove('familiesword2vec/"AA_kinase".tri')
newfile=open('familiesword2vec/"AA_kinase".tri')
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
print len(negative_sequences)
posnegrep=positive_sequences+negative_sequences
posneglabels=positive_labels+negative_labels
print len(posnegrep),len(posneglabels)
svmcrossvalidation(posnegrep,posneglabels)

        

