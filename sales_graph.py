from dash import Dash, dcc, html
import pandas as pd
from plotly.express import line

app = Dash()

df = pd.read_csv('data/daily_sales_data_pink.csv')
df = df.groupby('date')['sales'].sum().reset_index()
df.columns = ['date', 'total_sales']
df= df.rename(columns={'total_sales':'sales'})

line_chart = line(df, x='date', y='sales', title="Pink Morsel Sales", labels={'date': "Date", 'sales': "Sales"})

visualisation = dcc.Graph(
    id="sales-graph",
    figure=line_chart
)

header = html.H1("Pink Morsel Visualiser", id="header")

app.layout = html.Div(
    [
        header,
        visualisation
    ]
)

if __name__ == "__main__":
    app.run(debug=True)