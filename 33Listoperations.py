#Create a list with 7 elements and perform following operations. Let the list be initialized with List1 any 5 city names;
#a) Append a new city name to the List
#b) Insert a city name at 4th index position
#c) Sort the list and print all elements
#d) Sort the elements of the list in descending order.
#e) delete last three elements using pop operation

list=["Hyderabad","indore","chennai","Delhi","Ahmedabad","Jaipur","Lucknow"]
print("MY original list : %s",list)
list.append("Newcity")
print("After appending new city %s" %list)

list.insert(4,"fourthcity")
print("After inserting at fourth postion %s" %list)

list2=sorted(list,key=len)
print("Sorted list : %s" %list2)

list3=sorted(list,key=len,reverse=True)
print("Sorted list in descending order: %s"  %list3)

list.pop()
list.pop()
list.pop()
print("After popping last 3 elements from original list:%s" %list)
