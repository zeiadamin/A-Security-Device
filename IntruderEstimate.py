import random
import getpass
import timeit
import time
import datetime

current_state = 0          
lock_state = 0             
def transition (char):
   global lock_state
   global current_state
   if lock_state == 0 and char == "5":
       lock_state += 1
   elif lock_state == 1 and char == "6":
       lock_state += 1
   elif lock_state == 2 and char == "1":
       lock_state += 1
   elif lock_state == 3 and char == "7":
       lock_state += 1
   elif lock_state == 4 and char == "6":
       lock_state += 1
   elif lock_state == 5 and char == "1":   
       lock_state = 0
       if current_state == 0:
        change_lock()
       else:
        print ("unlock")
   elif lock_state == 5 and char == "4":
       lock_state = 0
       if current_state == 1:
        change_lock()
       else:
        print ("lock")
   else:
       lock_state = 0

def change_lock ():
   global current_state
   if current_state == 0:
       current_state = 1
       print ("unlock")
   else:
       current_state = 0
       print ("lock")


##############################################
#Intruder Estimate
##############################################

input_list = []
print_list = []

#numberofTrials = 5
#j = 0
#count = 0
#sumcount = 0

#Genrating random number and using them as keys for the device then couting the amount of time it takes to run
#____________________________________________________________________________________________________________
#for i in range (0,numberofTrials):
#    print ("trial", i)
#    while current_state != 1:
#            print (lock_state)
#            count += 1
#            print (count)
#            transition(str(random.randint(0,9)))
#            if current_state == 1:
#                current_state = 0
#                sumcount = sumcount + count
#                count = 0
#    i += 1
#print (sumcount/numberofTrials)

#### NOTES ####
#when generating random number of keys and running the keypad assuming that it takes a second for each key to
#be entered the amount of seconds it took to unlock was 1112605 seconds

#the process was repeated 5 times and then the average was 1552734 seconds

#_______________________________________________________________________________________________________________

#Now we need to test the actual time it takes to intrude by taking time stamps using the time it module

count = 0
t = time.localtime()

st = time.time()
##print ("trial", i)
while current_state != 1:
        print (lock_state)
        count += 1
        print (count)
        transition(str(random.randint(0,9)))

#i += 1
et = time.time()
res = et - st

print (res)

#### NOTES ####
#hen we use the time module to estimate the actual time it takes to break into the device the result was 16.125 seconds
#but since it's a random distribution we need to generate multiple tests then average the time
#_______________________________________________________________________________________________________________

#we need to generate multiple tests then average the time

#numberoftrials = 5
#j = 0
#count = 0
#sumcount = 0
#totaltime = 0
#mint= 10000000
#maxt= 0

#for i in range(1, numberoftrials):
#    t = time.localtime()

#    st = time.time()
#    ##print ("trial", i)
#    while current_state != 1:
#            print (lock_state)
#            count += 1
#            print (count)
#            transition(str(random.randint(0,9)))
#            current_state = 0

#    et = time.time()
#    res = et - st
#    if res > maxt:
#        maxt = res
#    if res < maxt:
#        mint = res
#    i += 1
#    et = time.time()
#    res = et - st

#    print (res)


#averagetime = totaltime/numberoftrials
#print (maxt)
#print (mint)
#print (averagetime)

#### NOTES ####
#The min time it took to break in was: 11.500 seconds
#The maximum time it took to break in was:42.250 seconds
#The average time it took to break in was:26.

#_______________________________________________________________________________________________________________