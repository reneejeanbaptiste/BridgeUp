import matplotlib.pyplot as plt


x= [0815,0832,0849,0906,0923,0940,0957,1014]#the time the battery is used
y= [100,99,98,97,96,95,94,93]#the percentage of battery
plt.scatter(x,y)
plt.xlabel('The time of which the battery is used in miltary time')
plt.ylabel('The percentage of battery life')
plt.yticks(y)
plt.xticks(x)

plt.title('Battery usage in a day !')
plt.savefig('/Users/reneejeanbaptise/Documents/BridgeUP/DataViz/figures/myScatter.png')
plt.show()

