ff=open("families.txt")
seq_count =0
for i in ff:
    if seq_count not in [157730,320296,321547,156442,156443,195552,269564]:
        print i,
    seq_count += 1
