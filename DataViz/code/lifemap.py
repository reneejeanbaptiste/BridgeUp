import plotly.plotly as ply
import pandas as pd
import pycountry

ply.sign_in('reneej','zpdf29jw3s')

lifedata= pd.read_csv('lifedata.csv')

for col in lifedata.columns:
	lifedata[col] = lifedata[col].astype(str)

 # plotly takes its arguments in dictionary format

geo_deets = dict(
		showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )

map_layout = dict(
	title = 'Life Expectancy Around the World',
	geo = geo_deets
	)

violet_scale = [[0.0, 'rgb(0,0,255)'], [0.25, 'rgb(0,233,255)'], [0.5, 'rgb(171,255,0)'], [0.75, 'rgb(255,109,0)'], [1.0, 'rgb(255,0,0)']]


input_countries =lifedata['COUNTRY']

countries = {}
for country in pycountry.countries:
	# if(country.alpha3 == "TZA"):
	# 	print country.name
    
	countries[country.name] = country.alpha3

codes = [countries.get(country, 'Unknown code') for country in input_countries]

# print ("codes" + str(codes))

lifedata['code'] = codes



lifedata['text'] = lifedata['COUNTRY']

stuff_plotly_needs = [ dict(
		type = 'choropleth',
		colorscale = violet_scale,
		autocolorscale = False,
		locations = lifedata['code'],
		z = lifedata['FEMALE'].astype(float),
		text = lifedata['text'],
		marker = dict(
			line = dict(
				color = 'rgb(255,255,255)',
				width = 1
				)
			),
		colorbar = dict(
			title = 'Life Expectance Rate'
			)
	)]
plotly_fig = dict(
	data = stuff_plotly_needs,
	layout = map_layout
	)

ply.plot(plotly_fig, filename = 'life_expectancy')