d={'a':0,'e':0,'i':0,'o':0,'u':0}
s="vishnu"
for seq in s:
    if seq=='a':
        d['a']+=1
    elif seq=='e':
        d['e']+=1
    elif seq=='i':
        d['i']+=1
    elif seq=='o':
        d['o']+=1
    elif seq=='u':
        d['u']+=1
list1=list(d.keys())
list2=list(d.values())
print("Vowels are : ")
for s in d:
        if d[s]>0:
            print("%c = %d" %(s,d[s]))
    
print("Total count of vowels %d" %sum(list(d.values())))         
