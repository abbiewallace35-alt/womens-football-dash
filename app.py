
from dash import Dash, html, dcc, Input, Output, State, callback
import dash

# Initialise Dash with multi-page support
app = Dash(__name__, use_pages=True)

DASHBOARD_NAME = "My Dashboard"
VERSION = "v0.1.0"

# Main layout
app.layout = html.Div(
    children=[
        # Header
        html.Div(
            className="header",
            children=[
                html.Div(
                    className="header-title",
                    children=[
                        html.H2(DASHBOARD_NAME),
                        html.Span(VERSION),
                    ],
                ),

                # Page selection dropdown
                dcc.Dropdown(
                    id="page-dropdown",
                    options=[
                        {"label": "Matches", "value": "/"},
                        {"label": "Players", "value": "/player-page"},
                        {"label": "Teams", "value": "/team-page"},
                    ],
                    value="/",
                    clearable=False,
                    className="page-dropdown",
                ),
            ],
        ),

        # Tracks the browser URL
        dcc.Location(id="page-url", refresh="callback-nav"),

        # Displays the selected page
        html.Div(
            dash.page_container,
            className="page-content",
        ),
    ]
)


# Navigate when dropdown changes
@callback(
    Output("page-url", "pathname"),
    Input("page-dropdown", "value"),
    prevent_initial_call=True,
)
def navigate_to_page(selected_page):
    return selected_page


# Keep dropdown synced with the current URL
@callback(
    Output("page-dropdown", "value"),
    Input("page-url", "pathname"),
)
def sync_dropdown(pathname):
    return pathname


if __name__ == "__main__":
    app.run(debug=True)
