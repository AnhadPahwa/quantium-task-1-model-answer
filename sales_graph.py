from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

app = Dash()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('data/daily_sales_data_pink.csv')

fig = px.bar(df, x='date', y='sales', color='region', barmode='group')

fig.update_layout(
    plot_bgcolor = colors['background'],
    font_color = colors['text'],
    paper_bgcolor = colors['background']
)

app.layout = html.Div(style = {'backgroundColor' : colors['background']}, children = [
    html.H1(
        children = "Pink Morsel Sales Data",
        style = {
            'textAlign' : 'center',
            'color': colors['text']
        }
    ),

    html.H1(children='Pink Morsel Sales Data by Date, filtered by region.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

app.run(debug=True)