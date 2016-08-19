import plotly.plotly as ply
import pandas as pd

ply.sign_in('reneej','zpdf29jw3s')

datav = pd.read_csv('data_v.csv')

for col in datav.columns:
	datav[col] = datav[col].astype(str)

#plotly takes its arguments in dictionary format

geo_deets = dict(
		showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'Mercator'
        )
    )

map_layout = dict(
	title = 'UV Radiation Levels Across the World',
	geo = geo_deets
	)

violet_scale = [[0.0, 'rgb(0,0,255)'], [0.25, 'rgb(0,233,255)'], [0.5, 'rgb(171,255,0)'], [0.75, 'rgb(255,109,0)'], [1.0, 'rgb(255,0,0)']]

datav['text'] = datav['COUNTRY (DISPLAY)']

stuff_plotly_needs = [ dict(
		type = 'choropleth',
		colorscale = violet_scale,
		autocolorscale = False,
		locations = datav['COUNTRY (CODE)'],
		z = datav['Display Value'].astype(float),
		text = datav['text'],
		marker = dict(
			line = dict(
				color = 'rgb(255,255,255)',
				width = 1
				)
			),
		colorbar = dict(
			title = 'UV radiation level'
			)
	)]
plotly_fig = dict(
	data = stuff_plotly_needs,
	layout = map_layout
	)

ply.plot(plotly_fig, filename = 'UVradiationlevel')