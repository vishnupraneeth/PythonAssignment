#Create Tuple as specified below;
#a) Create a Tuple tup1 with days in a week & print the tuple elements
#b) Create a Tuple tup2  with months in a year and concatenate it with tup1
#c) Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater.
#d) Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 notice the error type you get.
#e) Insert new element in to tuple by typecasting it to List

tup1=("Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday " , "Saturday" , "Sunday")
print(tup1)

tup2=("Jan","feb","mar","apr","may","june","july","aug","sept","oct","nov","dec")

print(tup2)

tup2=tup2+tup1

print("After appending :{}".format(tup2,))
print("After appending :%s" %(tup2,))

tuple1=(6,2,9)
tuple2=(10,1,2)
tuple3=(0,10,1)

print(tuple1,tuple2,tuple3)

tuple4=(max(tuple1),max(tuple2),max(tuple3))
print("Max ele among 3 tuples is {}".format(max(tuple4),))

# Removing a item from tuple is not possible as tuple is immutable.
#print("deleting tuple tuple1")
#del tuple1
#print("del : {}".format(tuple1,))

print("Insert new element in to tuple by typecasting it to List")
tuplist=()
list1=list(tuplist)
list1.append(1)
list1.append(2)
tuplist=tuple(list1)
print(tuplist)




