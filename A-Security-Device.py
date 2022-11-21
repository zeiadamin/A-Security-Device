#We need to design a lock system where the user keep entering characters and these characters will unlock the system
#if the user enter the correct code in a row 

#Ex:
#913520334412451033444123970001112334451334410101
#  unlock--^         ^--lock        unlock--^

#561761 is the unlocking code
#561764 is the locking code

#__________________________________________________________________________
#This will happen taking a Finite Automata approach where there are states and keys and if the key is correct
#the state will move to the next

#__________________________________________________________________________
#To Achieve that we need to keep track of the current_State (q0,q1,q2,q3,q4,q5) and we also need to keep track if
#the system is locked or unlocked let's  call that the lock_State

#__________________________________________________________________________
#To Start we need to get input from the user
#input_string = input()

#we need to set initial values for the current_state and the lock_state let's assume that the initial state of the
#system is locked
#0 is locked and 1 is unlocked
current_state = 0          
 
#the possible lock states are (0,1,2,3,4,5,6) where when you achieve 6 (up the ladder) and when that happen you
#switch the current_state and then you reset the lock_state to 0
lock_state = 0             

#now we need to start thinking about the logic of the of the code itself 
#we need to make sure that whenever we have a new input we need to check if the input is correct or not and change
#the state of the current_State and the lock_State as needed 
#to handle this we need to have a function that handles this change of state and also handles the input checking 

#Transition function that takes the user input as an argument and deals with the changes in the current_State
#and lock_State


def transition (char):
   global lock_state
   global current_state
   if lock_state == 0 and char == 5:
       lock_state += 1
       print (lock_state)
   elif lock_state == 1 and char == 6:
       lock_state += 1
       print (lock_state)
   elif lock_state == 2 and char == 1:
       lock_state += 1
       print (lock_state)
   elif lock_state == 3 and char == 7:
       lock_state += 1
       print (lock_state)
   elif lock_state == 4 and char == 6:
       lock_state += 1
       print (lock_state)
   elif lock_state == 5 and char == 1:
       lock_state = 0
       print (lock_state)
       change_lock() #a function that changes the current_state and print the the change in state
   elif lock_state == 5 and char == 4:
       lock_state = 0
       print (lock_state)
       change_lock() #a function that changes the current_state and print the the change in state
   else:
       lock_state = 0
       print (lock_state)

#A function that changes the current_State and print the the change in state
def change_lock ():
   global current_state
   if current_state == 0:
       current_state = 1
       print ("unlock")
   else:
       current_state = 0
       print ("lock")


#testing out the transition function and the change lock function 
print ("5 is entered")
transition (5)
print ("6 is entered")
transition (6)
print ("1 is entered")
transition (1)
print ("7 is entered")
transition (7)
print ("6 is entered")
transition (6)
print ("1 is entered")
transition (1)
print ("3 is entered")
transition (3)
print ("5 is entered")
transition (5)
print ("6 is entered")
transition (6)
print ("4 is entered")
transition (4)
print ("7 is entered")
transition (7)
print ("6 is entered")
transition (6)
print ("4 is entered")
transition (4)
print ("1 is entered")
transition (1)



#now since we have all fuctions ready we just need to make a for loop where as long as the user has input the
#transition function will be invoked 
#for char in input_string:
#    Transition (char)
    