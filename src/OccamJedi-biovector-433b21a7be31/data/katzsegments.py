import glob
from nltk import ngrams
from nltk.corpus import brown
from nltk.probability import LidstoneProbDist, WittenBellProbDist
from nltk.model.ngram import NgramModel
lid_estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
##Need to create 7027 left models
def leftmodel(sequencesinfamilylist):
    print 'Learning left model...'
    model_left = NgramModel(3, sequencesinfamilylist, pad_left=False, pad_right=True,estimator=lid_estimator)
    print 'Done learning left model.'
    return model_left
##Need to create 7027 right models
def rightmodel(sequencesinfamilylist):
    print 'Learning right model...'
    model_right = NgramModel(3, sequencesinfamilylist, pad_left=True, pad_right=False,estimator=lid_estimator)
    print 'Done learning right model.'
    return model_right
listoffamilies=glob.glob('../../familieswithsegmentsnew/*.seg')
#print listoffamilies
leftfamilymodellist=[]
rightfamilymodellist=[]
for j in range(len(listoffamilies)):
    f=open(listoffamilies[j])
    for i in f:
        gg=i[:-1].split("\t")
        l=[]
        for jj in gg:
            if len(jj) > 1:
                l.append(jj)
        if len(l) == 0:
            filename=listoffamilies[j].split("/")[-1].replace("seg","txt")
            print filename
            f=open("../../familiessequences/"+filename)
            lm=[]
            for i in f:
                lm.append(i[:-1])
            l=''.join(lm)
            l=ngrams(l,3)
    leftfamilymodellist.append(leftmodel(l))
    #rightfamilymodellist.append(rightmodel(l))

for i in range(len(listoffamilies)):
    tri_grams = ngrams("MAMAMRSTFAARVGAKPAVRGARPASRMSCMAYKVTLKTPSGDKTIECPADTYILDAAEEAGLDLPYSCRAGACSSCAGKVAAGTVDQSDQSFLDDAQMGNGFVLTCVAYPTSDCTIQTHQEEALY",3)
    print leftfamilymodellist[i].entropy(tri_grams)
    #print rightfamilymodellist[i].entropy(tri_grams)

