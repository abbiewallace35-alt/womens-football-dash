from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

df = px.data.iris()

fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    title="My First Dashboard"
)

app.layout = html.Div([
    html.H1("My Plotly Dash Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)