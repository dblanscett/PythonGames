#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Author: Devan Blanscett
' Program name: Random Number Generator
' Program Description: This program Generates as many random whole numbers as a user desires.
'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#code body here

class RandNumGen:
	def menu(self):
		

while True:
	menuInt = input("Menu:\n1: Generate random numbers\n2: Exit\n")
	Rand=RandNumGen()
	if menuInt == "2":
		break
	elif menuInt == "1":
		Rand.menu()
	else:
		print("Input not recognized, please enter 1 or 2")
