#Create 3 Lists (list1, list2, list3) with integer and perform following operations
#a) Create Maxlist by taking 2 maximum elements from each list.
#b) Find average value from all the elements of Maxlist.
#c) Create a MinlIst by taking 2 minimum elements from each list 
#d) Find the average value from all the elements of Minlist

list1=[2,6,7,1]
list2=[100,200,500,300]
list3=[8,1,0,9]
print(list1,list2,list3)
list1.sort()
list2.sort()
list3.sort()

Maxlist=[list1[-1],list1[-2],list2[-1],list2[-2],list3[-1],list3[-2]]
print("Max list : %s" %Maxlist)
Minlist=[list1[0],list1[1],list2[0],list2[1],list3[0],list3[1]]
print("Min list : %s" %Minlist)
MaxAvg  = sum(Maxlist)/len(Maxlist)
print("Avg of max list : %d" %MaxAvg)

MinAvg  = sum(Minlist)/len(Minlist)
print("Avg of max list : %d" %MinAvg)

