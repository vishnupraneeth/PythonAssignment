#Write a program to perform following operations on List. Create three lists as List1, List2 and List3 having 5 city names each list.
#a. Find the length city of each list element and print city and length
#b. Find the maximum and minimum string length element of each list
#c. Compare each list and determine which city is biggest & smallest with length.
#d. Delete first and last element of each list and print list contents.

list1=["Hyderabad","indore","chennai","Delhi","Ahmedabad"]
list2=["Jaipur","Lucknow","Kanpur","Nagpur","Bhopal"]
list3=["Rajkot","Ghaziabad","Vadodara","Thane","Patna"]
count=0
print("Pgm to find the length city of each list element and print city and length")
for ele in list1:
    
    count+=1
    print(" %d City name in list1 is %s and its length is %d" %(count,ele,len(ele)))
    
ids=0
for ele in list2:
    ids+=1
    print(" %d City name in list2 is %s and its length is %d" %(ids,ele,len(ele)))
    
ct=0
for ele in list3:
    ct+=1
    print(" %d City name in list3 is %s and its length is %d" %(ct,ele,len(ele)))
    

print("Pgm to find the maximum and minimum string length element of each list")
l1=sorted(list1,key=len)
l2=sorted(list2,key=len)
l3=sorted(list3,key=len)
print(list1)
print("min lenght list1 : %s and max length : %s" % (l1[0],l1[-1]))
print("min lenght list2 : %s and max length : %s" % (l2[0],l2[-1]))
print("min lenght list2 : %s and max length : %s" % (l3[0],l3[-1]))

print("Pgm to find the maximum and minimum string length element of all lists")
list5=[list1[-1],list2[-1],list3[-1]]
l6=sorted(list5,key=len)
print("Maximum element in all the lists is %s" %l6[-1])

list6=[list1[0],list2[0],list3[0]]
l7=sorted(list6,key=len)
print("Minimum element in all the lists is %s" %l7[0])

list1.pop(0)
list1.pop(-1)
print("After deleting firs and last element of list 1 %s" %list1)
list2.pop(0)
list2.pop(-1)
print("After deleting firs and last element of list 2 %s" %list2)
list3.pop(0)
list3.pop(-1)
print("After deleting firs and last element of list 3 %s" %list3)



