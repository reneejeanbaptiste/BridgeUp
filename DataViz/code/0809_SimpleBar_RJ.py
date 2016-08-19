# import matplotlib.pyplot as plt
# import numpy as np 

# years = np.arange(2012,2015)
# values = [2,5,9]
# plt.barh(years, values)
# plt.savefig('/Users/reneejeanbaptise/Documents/BridgeUP/DataViz/figures/simpleBar.png')
# plt.show()
 
#bar graph
# import matplotlib.pyplot as plt
# import numpy as np
# years = np.arange(2012,2015)
# category1_values = [2, 5, 9]
# category2_values = [7, 6, 3]
# plt.bar(years - 0.2,
#         category1_values,
#         color='blue',
#         edgecolor='none',
#         width=0.4,
#         align='center',
#         label='y1')
# plt.bar(years + 0.2,
#         category2_values,
#         color='orange',
#         edgecolor='none',
#         width=0.4,
#         align='center',
#         label='y2')
# plt.xticks(years, [str(year) for year in years])
# plt.ylabel('Units')
# plt.xlabel('Years')
# plt.title('This is a bar graph')
# plt.legend()
# #can change location with loc='lower right' or 'upper left' etc
# plt.show()
# plt.close()

#line graph
 import matplotlib.pyplot as plt
 time = [0,16,32,48,64,80]
 popDens = [.028,.047,.082,.141,.240,.381]
 plt.plot(time,popDens)
 plt.xlabel('Time (minutes)')
 plt.ylabel('Population Density')
 plt.title('Growth Rate of \nVibrio natriegens Bacteria')
 plt.savefig('...simpleLine.png')
 plt.show()
 plt.close()

#pie
# import matplotlib.pyplot as plt
# slices = [7,2,4,10]
# activities = ['Eat', 'poo', 'sleep', 'School']
# cols = ['blue', 'brown', 'yellow', 'red']

# #with pie charts, you should always set the figure size to two of the same values, otherwise it is distorted
# plt.figure(figsize =(4,4))

# #autopct puts the values on the chart for easy readability!
# plt.pie(slices, labels = activities, colors = cols, startangle = 90, 
# autopct = '%1.1f%%')
# #(more info on autopct at http://stackoverflow.com/questions/6170246/how-do-i-use-matplotlib-autopct?rq=1)

# plt.title('Time spent on Daily Activites')
# plt.savefig('/Users/reneejeanbaptise/Documents/BridgeUP/DataViz/figures/simplePie.png')
# plt.show()

# Hisrogram
# import matplotlib.pyplot as plt
# import 	numpy as np

# x = np.random(4,5,9,16,9,5)
# plt.hist()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.random.randn(1000) # x postion of stars
# y = np.random.randn(1000) # x postion of stars

# plt.hexbin(x,y)
# plt.show()
