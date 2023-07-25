#!/Library/Frameworks/Python.framework/versions/3.9/bin/python3

import numpy as np

testDict={'name':'susan','age':13,'hobby':'sports'}
print(testDict['name'])
print(testDict.get('age'))

testArray=[testDict,testDict] #can you create an array of dictionaries? yes
namesArray=['billy','joel']

print(testArray[0]['hobby'])
print("test array is of type: ", type(testArray))

#bnkArrTest=np.empty(10,dtype=float)   
#print(bnkArrTest)

'''
for num,obj in enumerate(testArray): #enumerate returns index,item in array
	obj['name']=namesArray[num]
	print(obj['name'],num)
for i in testArray:
	i['name']='bob'
for k in testArray:
	print(i['name'])
'''
