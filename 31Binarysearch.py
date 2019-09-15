# Binary seach

list=[]

n=int(input("Enter the number of elements "))
print("Enter %d elements now " %n)
flag=0
for i in range(n):
    a=int(input())
    list.append(a)

list.sort()
print("list is sorted " , list)
key=int(input("Enter the element you need to seach in the list"))

import math
k=0
n=n-1
while(k<=n):
    

    mid=math.ceil((k+n)/2)
    print("mid element is %d" %mid)
    if key==list[mid]:
        print("Successful search, your element is at position %d" %mid)
        flag=1
        break
    elif key<list[mid]:
            n=mid-1
    elif key>list[mid]:
            k=mid+1
    
if flag==0:
    print("Unsucessfull search, Desired element is not present in the list ")
