import glob
from nltk import ngrams
from nltk.corpus import brown
from nltk.probability import LidstoneProbDist, WittenBellProbDist
from nltk.model.ngram import NgramModel
lid_estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
##Need to create 7027 left models
def leftmodel(sequencesinfamilylist):
    print 'Learning left model...'
    model_left = NgramModel(3,ngrams(sequencesinfamilylist,3), pad_left=False, pad_right=True,estimator=lid_estimator)
    print 'Done learning left model.'
    return model_left
##Need to create 7027 right models
def rightmodel(sequencesinfamilylist):
    print 'Learning right model...'
    model_right = NgramModel(3, ngrams(sequencesinfamilylist,3), pad_left=True, pad_right=False,estimator=lid_estimator)
    print 'Done learning right model.'
    return model_right
listoffamilies=glob.glob('../../familiessequences/*.txt')
leftfamilymodellist=[]
rightfamilymodellist=[]
for j in range(len(listoffamilies)):
    f=open(listoffamilies[j])
    l=[]
    for i in f:
        l.append(i[:-1])
    lm=''.join(l)
    leftfamilymodellist.append(leftmodel(lm))
    rightfamilymodellist.append(rightmodel(lm))

for i in range(len(listoffamilies)):
    print leftfamilymodellist[i].entropy(["NLK","WTR","RET"])
    print rightfamilymodellist[i].entropy(["AAA","PPP","RE"])

