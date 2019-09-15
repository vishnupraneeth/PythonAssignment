#Create 3 dictionaries (dict1, dict2, dict3) with 3 elements each. Perform following operations
#a) Compare dictionaries to determine the biggest.
#b) Add new elements in to the dictionaries dict1, dict2
#c) print the length of dict1, dict2, dict3.
#d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.
dict1={1:1,2:2,3:3}
dict2={4:4,5:5,6:6,7:7}
dict3={8:8,9:9,10:10,11:11,12:12}

print(dict1.keys())
print(dict1.values())

#largest of each dictionary
print("a) Compare dictionaries to determine the biggest\n")
if(len(dict1)>len(dict2)):
    if(len(dict1)>len(dict3)):
        print("dict 1 is bigger compared to all dictionaries")
elif(len(dict2)>len(dict3)):
    print("dict2 is biggest compared to all dictionaries")
else:
    print("dict3 is biggest compared to all dictionaries")
    
    
  


#Adding new elements to dictionary
print("b) Add new elements in to the dictionaries dict1, dict2\n\n")
dict1.update({'New':"Address"})
print(dict1.items())

dict2.update({100:11})
print(dict2.items())

#Lenght of dict1 , dict2 , dict3
print("c) print the length of dict1, dict2, dict3.\n\n\n")
print("length of dict1 is {}".format(len(dict1)))
print("length of dict2 is {}".format(len(dict2)))
print("length of dict3 is {}".format(len(dict3)))

#Dictionary to string conversion
print("d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.\n\n")
s=str(dict1)
print(s)
print(type(s))

s1=str(dict2)
s2=str(dict3)

print("All dictionaries are converted into strings and resulted concatination is {}".format(s+s1+s2))

