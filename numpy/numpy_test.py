Created on Sat Oct 31 22:42:01 2015

@author: qian.sun
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
points = np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
print ys
z = np.sqrt(xs**2+ys**2)
plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar
plt.title("lll")

xarr =np.array([1.1,1.2,1.3,1.4,1.5])
yarr =np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True,False,True,True,False])
result =[(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
print result
result = np.where(cond,xarr,yarr)
print result
arr =np.random.rand(4,4)
print arr
print arr.mean(axis=1)
print "sum",arr.sum()
arr2 = np.random.rand(5)
print arr2
arr2.sort()
print arr2
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[6,23],[-1,7],[8,9]])
print x.dot(y)

img = imread('3344.jpg')
print (img.shape)
print img