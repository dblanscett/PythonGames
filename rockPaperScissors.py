#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Author: Devan Blanscett
' Program name: Rock Paper Scissors
' Program Description: This is a simple script to play rock, paper, scissors against the computer
'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#code body here

from random import randint
import os

computerChoice = randint(1,3)#computer chooses rock, paper or scissors

def printOutput(number):#reduces number of if/then statements
	number=int(number)#catches errors
	if number == 1:
		print("rock\n")
	elif number == 2:
		print("paper\n")
	elif number == 3:
		print("scissors\n")
	else:
		print("broken\n")
	
def whoWon(comp, usr):#input is computer choice and user choice
	if comp == usr:
		print("Tie game!\n")
	elif (comp+1) % 3 == usr:
		print("You won!\n")
	else:
		print("Computer won!\n")

while computerChoice:#will only end with input of 'n' or 'no' when asked to play again
	
	os.system('clear')#for readibility 

	userChoice = input("Choose your weapon\n1: Rock\n2: Paper\n3: Scissors\n")
	print("You Chose: ")
	printOutput(int(userChoice))	
	
	print("Computer chose: ")
	printOutput(computerChoice)
	
	whoWon(computerChoice,int(userChoice))
	
	computerChoice=randint(1,3)#reset for next round
	playAgain = input("do you want to play again(y/n): ")
	if playAgain == 'n' or playAgain == 'no':
		break

	

