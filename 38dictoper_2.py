#Create 2 dictionaries as follows;
#dict1 ={'Name':'Ramakrishna','Age':25}
#dict2={'EmpId':1234,'Salary':5000}
#Perform following operations   
#a) Create single dictionary by merging dict1 and dict2
#b) Update the salary to 10%
#c) Update the age to 26
#d) Insert the new element with key "grade" and assign value as "B1"
#e) Extract and print all values and keys separately.
#f) delete the element with key 'Age' and print dictionary elements.

dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}
def Merge1(dict1,dict2):
    dict3={**dict1 , **dict2}
    return dict3

res=Merge1(dict1,dict2)
print("After merging {}".format(res))

dict2["Salary"]+=dict2["Salary"]*0.1
print("After incrementing the salary by 10% :{}" .format(dict2["Salary"]))

dict1["Age"]=26
print("After updating the Age constraint :{}".format(dict1["Age"]))

res.update({"grade":"B1"})
print("Insert the new element with key grade and assign value as B1:{}".format(res))

print("Extracting and printing keys:{}".format(res.keys()))
print("Extracting and printing values :{}".format(res.values()))

del dict1["Age"]

print("After deleting Age constraint from dictionary :{}".format(dict1))
