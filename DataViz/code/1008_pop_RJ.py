import matplotlib.pyplot as plt
import sqlite3
import csv 


f = open('popByCountry.csv', 'rU')
data = csv.reader(f)
a = data.next()
a1 = []
for i in range(1,len(a)):
	a1.append(a[i])

years = [int(i) for i in a1]
print(years)

y = []
country = []
for i in data:
	print("i ",i)
	sub_y = []
	country.append(i[0])
	for a in range(1, len(i)):
		print("a ",a)
		if i[a] != '--' and i[a] != 'NA':
			sub_y.append(float(i[a]))
		else:
			sub_y.append(0)
	y.append(sub_y)	

print(y)
print(country)

for country_pop in y:
	plt.plot(years, country_pop)

plt.xlabel('Years')
plt.ylabel('Population (Millions)')
plt.title('Population By Country From Year 1980-2010')
plt.show()














