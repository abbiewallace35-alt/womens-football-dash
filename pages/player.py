
import dash
from dash import html

dash.register_page(
    __name__,
    path="/player-page",
    name="player_page"
)

layout = html.Div([
    html.H1("Player"),
])
