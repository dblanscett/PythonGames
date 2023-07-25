#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import keyboard
import os
from time import sleep

'''
test=input('int test')
if int(test):
	print("true")
else:
	print("false")
'''

MenuVariable=1

while MenuVariable>0:
	os.system('clear')
	print("Please make a selection:\n","1: Test input\n","0: Quit\n")
	MenuVariable=int(input())
	if MenuVariable==1: 
		inputTest=input("this is to test input: ")
		print(inputTest)
		sleep(2.5)
	else:
		MenuVariable=0
