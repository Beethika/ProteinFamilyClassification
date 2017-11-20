from nltk import ngrams
def trigramcreator(string):
    overlappingtrigrams=[]
    sample_seq=ngrams(string,3)
    tri_grams = list(sample_seq)
    for i in range(0,len(tri_grams),3):
        #print(tri_grams[i])
	overlappingtrigrams.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])   
    return overlappingtrigrams
def trigramcreator1(string):
    overlappingtrigrams=[]
    sample_seq=ngrams(string,3)
    tri_grams = list(sample_seq)
    for i in range(1,len(tri_grams),3):
	overlappingtrigrams.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
    return overlappingtrigrams
def trigramcreator2(string):
    overlappingtrigrams=[]
    sample_seq=ngrams(string,3)
    tri_grams = list(sample_seq)
    for i in range(2,len(tri_grams),3):
	overlappingtrigrams.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
    return overlappingtrigrams
def segmentandtrigramcreator(aList):
	dupind = []
	separatelist=[]
	singlelist = {}
	for i, v in enumerate(aList):
	    if len(v) >1:
		dupind.append(i)
	    else:
		pass
	for i in range(1,len(dupind)):
	    #print i-2, aList[dupind[i-2]]
	    if dupind[i] - dupind[i-1] >1:
		#print aList[dupind[i-1]]
		singlelist[dupind[i-1]+1]= aList[dupind[i-1]+1:dupind[i]]
		#print aList[dupind[i-1]+1:dupind[i]] #dupind[i-1],dupind[i],
		#print aList[dupind[i]]
	#for idx in dupind:
	#    print idx, aList[idx]
	if len(dupind) != 0:
	    if len(aList[0:dupind[0]])>3:
                separatelist.extend(trigramcreator(''.join(i for i in aList[0:dupind[0]])))
	    else:
	        separatelist.extend([''.join(i for i in aList[0:dupind[0]])])
	for idx in range(len(aList)):
	    if idx in dupind:
		separatelist.append(aList[idx])
	    elif idx in singlelist:
		if len(singlelist[idx]) > 3:
		    separatelist.extend(trigramcreator(''.join(i for i in singlelist[idx])))
		else:
		    separatelist.extend([''.join(i for i in singlelist[idx])])
	if len(dupind) != 0:
	    if len(aList[dupind[-1]+1:len(aList)])>3:
                separatelist.extend(trigramcreator(''.join(i for i in aList[dupind[-1]+1:len(aList)])))
	    else:
	        separatelist.extend([''.join(i for i in aList[dupind[-1]+1:len(aList)])])
	return separatelist
def segmentandtrigramcreator1(aList):
	dupind = []
	separatelist=[]
	singlelist = {}
	for i, v in enumerate(aList):
	    if len(v) >1:
		dupind.append(i)
	    else:
		pass
	for i in range(1,len(dupind)):
	    #print i-2, aList[dupind[i-2]]
	    if dupind[i] - dupind[i-1] >1:
		#print aList[dupind[i-1]]
		singlelist[dupind[i-1]+1]= aList[dupind[i-1]+1:dupind[i]]
		#print aList[dupind[i-1]+1:dupind[i]] #dupind[i-1],dupind[i],
		#print aList[dupind[i]]
	#for idx in dupind:
	#    print idx, aList[idx]
	if len(dupind) != 0:
	    if len(aList[0:dupind[0]])>3:
                separatelist.extend(trigramcreator1(''.join(i for i in aList[0:dupind[0]])))
	    else:
	        separatelist.extend([''.join(i for i in aList[0:dupind[0]])])
	for idx in range(len(aList)):	    
	    if idx in dupind:
		separatelist.append(aList[idx])
	    elif idx in singlelist:
		if len(singlelist[idx]) > 3:
		    separatelist.extend(trigramcreator1(''.join(i for i in singlelist[idx])))
		else:
		    separatelist.extend([''.join(i for i in singlelist[idx])])
	if len(dupind) != 0:
	    if len(aList[dupind[-1]+1:len(aList)])>3:
                separatelist.extend(trigramcreator1(''.join(i for i in aList[dupind[-1]+1:len(aList)])))
	    else:
	        separatelist.extend([''.join(i for i in aList[dupind[-1]+1:len(aList)])])
	return separatelist
def segmentandtrigramcreator2(aList):
	dupind = []
	separatelist=[]
	singlelist = {}
	for i, v in enumerate(aList):
	    if len(v) >1:
		dupind.append(i)
	    else:
		pass
	for i in range(1,len(dupind)):
	    #print i-2, aList[dupind[i-2]]
	    if dupind[i] - dupind[i-1] >1:
		#print aList[dupind[i-1]]
		singlelist[dupind[i-1]+1]= aList[dupind[i-1]+1:dupind[i]]
		#print aList[dupind[i-1]+1:dupind[i]] #dupind[i-1],dupind[i],
		#print aList[dupind[i]]
	#for idx in dupind:
	#    print idx, aList[idx]
	if len(dupind) != 0:
	    if len(aList[0:dupind[0]])>3:
                separatelist.extend(trigramcreator2(''.join(i for i in aList[0:dupind[0]])))
	    else:
	        separatelist.extend([''.join(i for i in aList[0:dupind[0]])])
	for idx in range(len(aList)):
	    if idx in dupind:
		separatelist.append(aList[idx])
	    elif idx in singlelist:
		if len(singlelist[idx]) > 3:
		    #print singlelist[idx]
		    separatelist.extend(trigramcreator2(''.join(i for i in singlelist[idx])))
		else:
		    separatelist.extend([''.join(i for i in singlelist[idx])])
	if len(dupind) != 0:
	    if len(aList[dupind[-1]+1:len(aList)])>3:
                separatelist.extend(trigramcreator2(''.join(i for i in aList[dupind[-1]+1:len(aList)])))
	    else:
	        separatelist.extend([''.join(i for i in aList[dupind[-1]+1:len(aList)])])
	return separatelist
f=open("segmentsfrword2vec.txt")
ll=[]
for i in f:
    gg=i[:-1].split("\t")
    #print gg
    for i in segmentandtrigramcreator(gg):
        print i+"\t",
    print "\n",
    for i in segmentandtrigramcreator1(gg):
        print i+"\t",
    print "\n",
    for i in segmentandtrigramcreator2(gg):
        print i+"\t",
    print "\n",
