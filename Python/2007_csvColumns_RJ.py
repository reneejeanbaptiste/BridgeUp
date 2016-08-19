import csv

hiv_in = open("hiv_swazi.csv","rU")
stats_in =  csv.reader(hiv_in)

#id the headeer soo we can find the year column 
column_header = stats_in.next()

year_index = column_header.index('Year')
print(stats_in.next())
def breakyear(year):
	for row in stats_in: 
		if row[year_index]==year:
			print(row)
breakyear(raw_input())
hiv_in.close()