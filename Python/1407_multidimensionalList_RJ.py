countryDisease = [('Sri Lanka','Lymphatic Filariasis',1000000000,2008),('Colombia','River Blindness',120000000,2013)]
countryDisease[1][2]

print('There were '+str(countryDisease[0][2])+' cases of '+str(countryDisease[0][1])+' in the country '+str(countryDisease[0][0]))
print('There were also '+str(countryDisease[1][2])+' cases of '+str(countryDisease[1][1])+' in the country '+str(countryDisease[1][0]))

for country in countryDisease:
	#for data in country:		
		print(country[3]) 