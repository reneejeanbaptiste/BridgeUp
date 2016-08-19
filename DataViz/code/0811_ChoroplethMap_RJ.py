import plotly.plotly as ply
import pandas as pd

#add your username an API key so we can take to plotly
ply.sign_in('reneej','zpdf29jw3s')


#this function returns a DataFrame, which is a two dimensional size mutable table
#abdtraction for noe but know that it is available to you 
food_production = pd.read_csv('https://catalog.data.gov/harvest/object/708bbe48-890c-4bc6-a473-8c0a0ffb2b6c')

for col in food_production.columns:
	food_production[col] = food_production[col].astype(str)

# plotly takes its arguments in dicionary formate

geo_deets  = dict(
	scope= 'USA', 
	projection = dict(type = 'albers usa'),
	showlakes = True,
	lakecolor = 'white'
	)


map_layout = dict(
	title = '2011 Production of Agriculture by State',
	geo= geo_deets
	)


violet_scale = [[0.0, 'rgb(0, 204, 204)'],[1.0, 'rgb(102, 204, 0']]


food_production['text'] = food_production['state'] + '<br> Beef : ' + food_production['beef']

stuff_plotly_needs = [ dict(

	type='choropleth',
	colorscale = violet_scale,
	autocolorscale= False,
	locations = food_production['code'],
	z= food_production['total exports'].astype(float),
	locationmode = 'USA-states',
	text = food_production['text'],
	marker = dict(
		line = dict(
			color= 'rgb(51, 0, 204)',
			width=2
		)),
	colorbar = dict(
		title = 'Million USD')
	) ]

plotly_fig = dict(
		data= stuff_plotly_needs,
		layout = map_layout
	)

ply.plot( plotly_fig, filename = 'awesome-choropleth-map')

ply.plot(plotly_fig, filename='awsome-sauce-map')