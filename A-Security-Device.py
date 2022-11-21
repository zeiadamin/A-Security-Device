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

#we need to set initial values for the current_State and the lock_State let's assume that the initial state of the
#system is locked
#0 is Locked and 1 is Unlocked
#current_State = 0          

#The possible lock states are (0,1,2,3,4,5,6) where when you achieve 6 (up the ladder) and when that happen you
#switch the current_State and then you reset the lock_State to 0
#lock_State = 0             

#now we need to start thinking about the logic of the of the code itself 
#we need to make sure that whenever we have a new input we need to check if the input is correct or not and change
#the state of the current_State and the lock_State as needed 
#to handle this we need to have a function that handles this change of state and also handles the input checking 

#Transition function that takes the user input as an argument and deals with the changes in the current_State
#and lock_State
# def Transition (char):
#   if lock_State == 0 and char == 5:
#       lock_State++
#   elif lock_State == 1 and char == 6:
#       lock_State++
#   elif lock_State == 2 and char == 1:
#       lock_State++
#   elif lock_State == 3 and char == 7:
#       lock_State++
#   elif lock_State == 4 and char == 6:
#       lock_State++
#   elif lock_State == 5 and char == 1:
#       lock_State = 0
#       Change_Lock() #A function that changes the current_State and print the the change in state
#   elif lock_State == 5 and char == 4:
#       lock_State = 0
#       Change_Lock() #A function that changes the current_State and print the the change in state
#   else:
#       lock_State = 0

#A function that changes the current_State and print the the change in state
# def Change_Lock ():
#   if current_State == 0:
#       current_State = 1
#       print ("unlock")
#   else:
#       current_State = 0
#       print ("lock")

#now since we have all fuctions ready we just need to make a for loop where as long as the user has input the
#transition function will be invoked 
#for char in input_string:
#    Transition (char)
    