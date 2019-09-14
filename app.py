import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import geopandas as gpd


mapbox_key = "pk.eyJ1Ijoic29jam9uIiwiYSI6ImNqenEwZDk4MjBqb3YzaG1tMmsycWEzZXkifQ.Zy16rF6eDSw9pqMA0R-b6Q"

vn_shp = 'data/geojson/vnm_polbnda_plyl_adm1_2014_pdc/vnm_polbnda_adm1_2014_pdc.shp'
vn_df = gpd.read_file(lep_shp)

#14.0583° N, 108.2772° E
# template for map
map_layout = {
    'title': 'Vietnam War',
    'data': [{
        'lon': 14.0583,
        'lat': 108.2772,
        'mode': 'markers',
        'marker': {
            'opacity': 0.0,
        },
        'type': 'scattermapbox',
        'name': 'Vietnam',
        # 'text': lep_df['HOVER'],
        # 'hoverinfo': 'text',
        # 'showlegend': True,
    }],
    'layout': {
        'autosize': True,
        # 'hovermode': 'closest',
        # 'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0},
        'mapbox': {
            'accesstoken': mapbox_key,
            'center': {
                'lat': lat,
                'lon': lon
            },
            'zoom': 8.0,
            'bearing': 0.0,
            'pitch': 0.0,
        },
    }
}











#Orginal code - keeping until I know better
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure={
#             'data': [
#                 {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                 {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#             ],
#             'layout': {
#                 'title': 'Dash Data Visualization'
#             }
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)