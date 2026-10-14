
import dash
from dash import html

dash.register_page(
    __name__,
    path="/team-page",
    name="team_page"
)

layout = html.Div([
    html.H1("Team"),
])