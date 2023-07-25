#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Author: Devan Blanscett
' Program name: Game engine template
' Program Description: Game engine template for turn based strategy board game 
'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
from time import sleep

class gameTitle:
	def __init__(s,numPlayers):
		s.maxNumPlayers = 6
		if numPlayers > s.maxNumPlayers:
			print("Number of players exceeds maximum capacity, set to ",s.maxNumPlayers," players")
			s.numPlayers = s.maxNumPlayers
		else:
			s.numPlayers = numPlayers
		s.numTurns = 10 #adjust according to number of players
		keys = ['name','color','attribute','modifier','resource','territory','units']
		values = ['','',1,1,5,1,0]
		s.playerDict = {key: value for key,value in zip(keys,values)}
		print(s.maxNumPlayers,s.numPlayers,s.numTurns)
		#print(s.playerDict)

	def getNamesAndColors(self):
		print("read in player's names and colors")

	def engine(self):
		playerTurn(2)#pass player index
		#will need to go through turn order for each player and track rounds
		print("gameplay")

	def playerTurn(self, whichPlayer):
		self.adjustUnitsAndAttributes(whichPlayer)
		print("turn step 1, turn step 2 turn step 3")
		self.adjustResources(whichPlayer)

	def adjustUnitsAndAttributes(self, whichPlayer):
		self.adjustModifies(whichPlayer)
		print("print costs and ask number built then update values")

	def adjustModifiers(self, whichPlayer):
		print("call after adjusting attributes")

	def adjustResources(self, whichPlayer):
		self.countTerritory(whichPlayer)

	def countTerritory(self, whichPlayer):
		print("ask player how much territory and adjust resources")

while True:#top menu loop
	os.system("clear")
	print("Top game menu\n")
	print("Chose an option from the menu:\n")
	print("1: Start new game\n2: Load existing game\n3: Settings\n4: Credits\n5: Exit\n")
	while True:#input error handling loop
		try:
			menuInput = int(input())
			if 0 < menuInput <= 5:
				break
			
		except ValueError:
			print("Please enter a numeric value corresponding to an option")		
		
	if menuInput == 1:
		while True:#error handling loop
			try:
				players=int(input("How many players?(between 2-6) "))
				game=gameTitle(players)
				break
			except ValueError:
				print("Please enter an integer for number from 2 to 6")
	if menuInput == 2:
		print("load")
		break
	elif menuInput == 3:
		print("settings")
		break
	elif menuInput == 4:
		print("credits")
		break
	elif menuInput == 5:
		break
a=gameTitle(3)
b=gameTitle(7)

