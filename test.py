#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Author: Devan Blanscett
' Program name: 
' Program Description: 
' 
'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#code body here
from numpy import array

x =array([3,2,1])
y = x
y[0]=0
print(type(x))
print(type(y))
print("x=",x)
print("y=",y)
print("I changed a thing")
