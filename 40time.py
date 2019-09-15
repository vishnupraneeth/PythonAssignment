#Using time module perform following operations.
#a) Print current time for every 5 seconds up to 1 minute time interval.
#b) Write a program to find out how much CPU time is taken for the execution of above(32.a)  program.
import time
#from datetime import datetime
#now=datetime.now()time = now.strftime("%H:%M:%S")
t1=time.time()
print("time:", t1)

count=0
def timemod():
    print("current time is {}".format(time.asctime()))

while count<=12:
    time.sleep(5)
    count+=1
    timemod()

#now2=datetime.now()
#time2=now2.strftime("%H:%M:%S")
t2=time.time()
print("end time",t2)
diff=t2-t1
print("CPU TIME TAKEN TO EXECUTE  THIS PROGRAM IS :{}".format(diff))
    
