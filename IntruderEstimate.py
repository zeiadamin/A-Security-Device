import random
import getpass
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

#A transition function that keeps track of the input key and the lock state and changes the current lock based on the
#Finite Automata logic
def transition (char):
   global lock_state
   global current_state
   if lock_state == 0 and char == "5":
       #now we are in the state q0 if the key is correct:6 then incement the state and move to state q1
       lock_state += 1
       #print (lock_state)
   elif lock_state == 1 and char == "6":
       #now we are in the state q1 if the key is correct:6 then incement the state and move to state q2
       lock_state += 1
       #print (lock_state)
   elif lock_state == 2 and char == "1":
       #now we are in the state q2 if the key is correct:6 then incement the state and move to state q3
       lock_state += 1
       #print (lock_state)
   elif lock_state == 3 and char == "7":
       #now we are in the state q3 if the key is correct:6 then incement the state and move to state q4
       lock_state += 1
       #print (lock_state)
   elif lock_state == 4 and char == "6":
       #now we are in the state q4 if the key is correct:6 then incement the state and move to state q5
       lock_state += 1
       #print (lock_state 
   elif lock_state == 5 and char == "1":   
       #now we are in the state q5 if the key is correct:6 then incement the state and move to state q6UNLOCK
       lock_state = 0
       #print (lock_state)
       if current_state == 0:
        change_lock() #a function that changes the current_state and print the the change in state
       else:
        print ("unlock")

   elif lock_state == 5 and char == "4":
       #now we are in the state q5 if the key is correct:6 then incement the state and move to state q6UNLOCK
       lock_state = 0
       #print (lock_state)
       if current_state == 1:
        change_lock() #a function that changes the current_state and print the the change in state
       else:
        print ("lock")

   else:
       #else then the key is wrong and the state is reset to q0
       lock_state = 0
       #print (lock_state)

#A function that changes the current_State and print the the change in state
def change_lock ():
   global current_state
   if current_state == 0:
       current_state = 1
       print ("unlock")
   else:
       current_state = 0
       print ("lock")


##############################################
#THE KEYPAD
##############################################

#A list that keeps track of actual inputs
input_list = []
#a list that keep track of number of inputs till 6 and prints *s
print_list = []

#A loop that is always working
while True:
    #getting the user keys
    user_input = getpass.getpass('')

    #ignoring input other than keys from 1 to 9
    if user_input in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        input_list.append(user_input)
        print_list.append("*")
        print (*print_list)
        transition(user_input)
    else:
        #in case of a wrong input print wrong character 
        print ("Wrong Character")

    #if the 6 digits are entrered but they are wrong then print wrong passcode
    if len(input_list) == 6:
        if input_list != ["5","6","1","7","6","1"]:
            if input_list != ["5","6","1","7","6","4"]:
                print ("wrong passcode")
        input_list = []
        print_list = []



    