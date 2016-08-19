import csv
import matplotlib.pyplot as plt
f = open('popByCountry.csv', 'rU')
data = csv.reader(f, delimiter= ',')

for row in data:
	print row[0]

# import matplotlib.pylot as pyl 
# import sqlite3
# import csv

# conn  = sqlite3.connect('popData.db')
# c = conn.cursor()

# f = open ('popByCountry.csv''rU')
# data = csv.reader(f)
# a = data.next()
# a1 = []
# for i in range(1,len(a)):
# 	a1.append(a[i])

# headers[int()] for i in a1
