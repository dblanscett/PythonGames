#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import matplotlib.pyplot as plt
from numpy import arange, sin, cos, pi

x = arange(-3*pi,3*pi,pi/12)
y = sin(x)
y2 = cos(x)

plot = plt.plot(x,y)
plt.show()
