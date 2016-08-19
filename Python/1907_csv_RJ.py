import csv 
f = open("hiv_swazi.csv",'rU')
data = csv.reader(f)

dataOut = open('hiv_swazi_out.csv ','w')
writeData = csv.writer(dataOut)

for line in data:
	writeData.writerow(line)


f.close
dataOut.close()

'''
#print(data.next()) *this prints a single row of code
#print(data. next())

#...
#for item in data:
#	print(item)

#for i in range(2)
#	print( str(i) +'  '+ data.next())
for row2 in data:
	print(row2[0])
''' 