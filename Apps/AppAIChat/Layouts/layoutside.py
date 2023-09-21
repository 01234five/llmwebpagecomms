from dash import html, dcc
import dash_mantine_components as dmc
from Apps.AppAIChat.Callbacks.CallbackAIChatSideTabs import (
    GetGraph1,
    GetLayoutSpecificUsers,
    GetLayoutOverallgroup,
)


def Render():
    return html.Div(
        [
            html.Div("Query data:", className="appaichatside-title"),
            dcc.Tabs(
                id="appaichatside-tabs",
                value="0",
                style={"marginTop": "10px"},
                children=[
                    dcc.Tab(
                        label="Overall Group",
                        children=[],
                        value="0",
                        className="appaichatside-tab-custom",
                        selected_className="appaichatside-tab-customselected-0",
                    ),
                    dcc.Tab(
                        label="Specific User",
                        children=[],
                        value="1",
                        className="appaichatside-tab-custom",
                        selected_className="appaichatside-tab-customselected-allothers",
                    ),
                ],
            ),
            html.Div(GetLayoutOverallgroup(), id="appaichatside-domelements-container"),
            html.Div([GetGraph1()], id="appaichatside-graph-container"),
        ],
        className="appaichat-side-container",
    )
