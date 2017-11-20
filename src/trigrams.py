from nltk import ngrams
#aList=['M', 'A', 'D', 'A', 'M', 'N', 'E', 'L', 'CNLTQ', 'H', 'L', 'Q', 'V', 'D', 'DDQLSNL', 'K', 'L', 'K', 'NGYSL', 'F', 'P', 'H', 'Q', 'E', 'K', 'V', 'M', 'L', 'W', 'M', 'K', 'Y', 'R', 'E', 'N', 'L', 'T', 'K', 'K', 'E', 'C', 'R', 'K', 'E', 'G', 'E', 'K', 'T', 'W', 'G', 'V', 'R', 'G', 'G']
sequence=['M', 'A', 'D', 'A', 'M', 'N', 'E', 'L', 'CNLTQ', 'H', 'L', 'Q', 'V', 'D', 'DDQLSNL', 'K', 'L', 'K', 'NGYSL', 'F', 'P', 'H', 'Q', 'E', 'K', 'V', 'M', 'L', 'W', 'M', 'K', 'Y', 'R', 'E', 'N', 'L', 'T', 'K', 'K', 'E', 'C', 'R', 'K', 'E', 'G', 'E', 'K', 'T', 'W', 'G', 'V', 'R', 'G', 'G', 'I', 'I', 'S', 'L', 'C', 'MGLGKTL', 'T', 'A', 'L', 'A', 'Y', 'S', 'F', 'Q', 'N', 'K', 'A', 'S', 'F', 'P', 'T', 'L', 'VITSKT', 'V', 'M', 'H', 'E', 'W', 'K', 'T', 'E', 'G', 'V', 'E', 'K', 'FFDSD', 'N', 'I', 'R', 'V', 'L', 'Y', 'L', 'H', 'R', 'DYIKN', 'IDKISR', 'D', 'D', 'I', 'M', 'T', 'Y', 'DIVITT', 'Y', 'D', 'V', 'C', 'L', 'F', 'A', 'C', 'K', 'K', 'G', 'N', 'Y', 'F', 'L', 'QCFEM', 'G', 'E', 'E', 'Q', 'S', 'L', 'M', 'K', 'N', 'K', 'I', 'V', 'A', 'I', 'H', 'TRKRK', 'D', 'A', 'N', 'L', 'P', 'N', 'L', 'K', 'G', 'T', 'A', 'V', 'I', 'Y', 'G', 'T', 'P', 'W', 'E', 'R', 'V', 'I', 'C', 'D', 'E', 'S', 'Q', 'K', 'F', 'A', 'N', 'P', 'K', 'T', 'M', 'T', 'Y', 'K', 'C', 'I', 'M', 'A', 'V', 'YGKYK', 'W', 'C', 'LTGTPIR', 'N', 'Y', 'E', 'T', 'D', 'I', 'W', 'A', 'Q', 'L', 'R', 'F', 'C', 'G', 'Y', 'K', 'G', 'V', 'E', 'R', 'S', 'H', 'D', 'WNRNG', 'Q', 'G', 'L', 'I', 'A', 'F', 'K', 'D', 'H', 'N', 'L', 'I', 'S', 'A', 'I', 'F', 'T', 'M', 'S', 'Y', 'D', 'D', 'A', 'Q', 'M', 'S', 'L', 'P', 'E', 'K', 'T', 'E', 'N', 'N', 'L', 'T', 'V', 'K', 'L', 'E', 'G', 'Q', 'H', 'KEIYE', 'G', 'I', 'L', 'T', 'E', 'T', 'R', 'E', 'M', 'Y', 'K', 'K', 'M', 'M', 'N', 'D', 'L', 'C', 'S', 'F', 'T', 'Y', 'V', 'L', 'A', 'M', 'F', 'T', 'R', 'L', 'R', 'Q', 'C', 'A', 'I', 'A', 'P', 'Y', 'L', 'I', 'T', 'P', 'D', 'A', 'K', 'R', 'N', 'SKEKKN', 'C', 'S', 'E', 'W', 'C', 'L', 'D', 'K', 'FGGAG', 'I', 'K', 'S', 'S', 'K', 'I', 'L', 'K', 'I']
def trigramcreator(string):
    overlappingtrigrams=[]
    sample_seq=ngrams(string,3)
    tri_grams = list(sample_seq)
    for i in range(0,len(tri_grams),3):
        #print(tri_grams[i])
	overlappingtrigrams.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
    for i in range(1,len(tri_grams),3):
	overlappingtrigrams.append(tri_grams[i][0]+tri_grams[i][1]+tri_grams[i][2])
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
	for i in range(2,len(dupind)):
	    #print i-2, aList[dupind[i-2]]
	    if dupind[i] - dupind[i-1] >1:
		#print aList[dupind[i-1]]
		singlelist[dupind[i-1]+1]= aList[dupind[i-1]+1:dupind[i]]
		#print aList[dupind[i-1]+1:dupind[i]] #dupind[i-1],dupind[i],
		#print aList[dupind[i]]
	#for idx in dupind:
	#    print idx, aList[idx]
	for idx in range(len(aList)):
	    if idx in dupind:
		separatelist.append(aList[idx])
	    elif idx in singlelist:
		if len(singlelist[idx]) > 2:
		    separatelist.extend(trigramcreator(''.join(i for i in singlelist[idx])))
		else:
		    separatelist.extend([''.join(i for i in singlelist[idx])])
	return separatelist
print segmentandtrigramcreator(sequence)
