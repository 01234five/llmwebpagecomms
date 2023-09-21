from dash.dependencies import Input, Output, State, ALL
from dash import no_update, dcc
import pandas as pd
import plotly.express as px
from dash import html, dcc
import dash_mantine_components as dmc


def RegisterCallback(_app):
    @_app.callback(
        Output("appaichatside-graph-container", "children", allow_duplicate=True),
        Output("appaichatside-domelements-container", "children", allow_duplicate=True),
        Input("appaichatside-tabs", "value"),
        prevent_initial_call=True,
    )
    def update_textarea_style(value):
        if value == None:
            return no_update
        if value == "0":
            return GetGraph1(), GetLayoutOverallgroup()
        if value == "1":
            return GetGraph1(), GetLayoutSpecificUsers()
        return no_update


def GetGraph1():
    superhero_theme_clrs = [
        "#FFD700",
        "#DC143C",
        "#50C878",
        "#FF00FF",
        "#FFA500",
        "#40E0D0",
        "#DAA520",
        "#00BFFF",
        "#DA70D6",
        "#FF6347",
        "#32CD32",
        "#FF1493",
        "#1E90FF",
        "#FFD700",
        "#9370DB",
        "#F08080",
    ]
    df = px.data.iris()
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        color_discrete_sequence=superhero_theme_clrs,
        size="petal_length",
        hover_data=["petal_width"],
        template="plotly_dark",
    ).update_layout(
        {
            "plot_bgcolor": "#1F2630",
            "paper_bgcolor": "#1F2630",
            "font": {"color": "white"},
        }
    )
    return dcc.Graph(
        id="crossfilter-indicator-scatter",
        hoverData={"points": [{"customdata": "Japan"}]},
        figure=fig,
        responsive=True,
    )


def GetLayoutOverallgroup():
    return [
        dmc.ChipGroup(
            [
                dmc.Chip(
                    "Survey",
                    value="Survey",
                    color="orange",
                    variant="filled",
                    classNames={
                        "label": "dmcchip-label",
                        "iconWrapper": "dmcchip-iconwrapper",
                        "checkIcon": "dmcchip-checkIcon",
                    },
                ),
                dmc.Chip(
                    "Questions",
                    value="Questions",
                    color="orange",
                    variant="filled",
                    classNames={
                        "label": "dmcchip-label",
                        "iconWrapper": "dmcchip-iconwrapper",
                        "checkIcon": "dmcchip-checkIcon",
                    },
                ),
            ],
            value="Survey",
            className="appaichat-dmcgroup-1",
        ),
    ]


def GetLayoutSpecificUsers():
    segementedcontroldata = []
    for x in range(99):
        segementedcontroldata.append({"value": str(x), "label": str(x)})
    return [
        html.Div(
            [
                dmc.SegmentedControl(
                    id="segmented",
                    value="0",
                    data=segementedcontroldata,
                    orientation="horizontal",
                    fullWidth=True,
                    sx={"overflowX": "auto"},
                ),
                dmc.Text(id="segmented-value"),
            ]
        ),
        dmc.ChipGroup(
            [
                dmc.Chip(
                    "Survey",
                    value="Survey",
                    color="orange",
                    variant="filled",
                    classNames={
                        "label": "dmcchip-label",
                        "iconWrapper": "dmcchip-iconwrapper",
                        "checkIcon": "dmcchip-checkIcon",
                    },
                ),
                dmc.Chip(
                    "Questions",
                    value="Questions",
                    color="orange",
                    variant="filled",
                    classNames={
                        "label": "dmcchip-label",
                        "iconWrapper": "dmcchip-iconwrapper",
                        "checkIcon": "dmcchip-checkIcon",
                    },
                ),
            ],
            value="Survey",
            className="appaichat-dmcgroup-1",
        ),
    ]
