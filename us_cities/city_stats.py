#%%

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def add_line(fig, value, color, name, df):
    
    max = df['population'].max()
    
    fig.add_trace(go.Scatter(x=[value,value], 
        y=[0,-max/10], 
        mode='lines', 
        line=dict(
            color=color, 
            width=2),
        name=name))

def make_graph(comparison_variable='density', comparson_unit='people/km<sup>2</sup>'):

    # key places
    suburb_min = 100
    suburb_max = 10000
    cedarburg = 925.5
    forest_hills = 13470
    ridgewood = 1688.6

    df = pd.read_csv("uscities.csv")
    df_cities = df[df['density'] > suburb_max]

    fig = px.histogram(df, x=comparison_variable, y='population', nbins=500, color_discrete_sequence = ['gray'])

    # fig.update_yaxes(type='log')

    mean = df[comparison_variable].mean()
    median = df[comparison_variable].median()

    mean_cities = df_cities[comparison_variable].mean()
    
    print (f'mean_cities:{mean_cities}')
    print (f'mean:{mean}')

    if comparison_variable == 'density':
        add_line(fig, suburb_max, 'tomato', 'suburb_max', df)
        add_line(fig, suburb_min, 'tomato', 'suburb_min', df)
        add_line(fig, mean, 'grey', 'mean', df)
        add_line(fig, median, 'black', 'median', df)
        add_line(fig, cedarburg, 'dodgerblue', 'Cedarburg, WI', df)
        add_line(fig, 2379, '#15546a', 'Milwaukee, WI', df)
        add_line(fig, forest_hills, 'seagreen', 'Forest Hills, NYC', df)
        add_line(fig, ridgewood, 'darkorange', 'Ridgewood, NJ', df)
        add_line(fig, 10800, 'goldenrod', 'NYC Average', df)

        fig.update_xaxes(range=[0, forest_hills*1.1])

    fig.update_layout(
        title={
            'text': f'US Cities {comparison_variable} ({comparson_unit})<br><sub>source:https://simplemaps.com/data/us-cities</sub>',
            'x': 0.5,
            'y': 0.95,
            'xanchor': 'center',
            'yanchor': 'top',
        },
        legend=dict(title='Legend Title'),
        showlegend=True,
        # xaxis=dict(title='Categories', domain=[0.1, 0.9]),
    )

    fig.show()

if __name__ == '__main__':
    make_graph()
    # make_graph(comparison_variable='population', comparson_unit='people')