import matplotlib.pyplot as plt


x= [2,4,6,8]
y= [1,3,5,9]
x2= [10,8,6,4]
y2= [1,3,5,7]
plt.plot(x,y, label= 'First Line', color="#FFAAB8" )
plt.plot(x2,y2, label= 'Second Line',color="#951732")
plt.xlabel('X-Axis Number')
plt.ylabel('Y-Axis Number')
plt.title('Awsome Graph\nCheck it out!')
#plt.plot([1,2,3],[1,2,3]
plt.legend()
plt.show()

