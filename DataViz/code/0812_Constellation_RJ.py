import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D


data = np.genfromtxt('wings.txt', usecols=(0,1,2))

x=[]
y=[]
z=[]

for point in data:
	x.append(point[0])
	y.append(point[1])
	z.append(point[2])



fig = plt.figure()
ax =  fig.add_subplot(111, projection='3d')
ax.scatter(z,x,y)
ax.axis(off)
plt.show