#21  Math and Random Modules Using the built-in functions on Numbers perform following operations
#a) Round of the given floating point number. Example:  n=0.543 then round it next decimal number, i.e n=1.0 Use round() function
#b) Find out the square root of a given number. (Use sqrt(x) function)
#c) Generate random number between 0, and 1 ( use  random() function)
#d) Generate random number between 10 and  500. (Use uniform() function)

import math
a=float(input("Enter a floating point number , i'll given the rounded value"))
print("you have entered {} and I rounded it to {}".format(a,math.ceil(a)))

a1=int(input("Enter a number for which you need to find the square root"))
print("Square root of the number which you have entered is :{}".format(math.sqrt(a1)))\

import random
print("random number between 0 and 1 is :{}".format(random.randrange(0,1)))
print("Generating random number between 10 and  500. (Use uniform() funct:{}".format(random.uniform(10,500)))



