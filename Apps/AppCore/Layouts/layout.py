from dash import html, dcc


def Render():
    return html.Div(
        [
            dcc.Location(id="url"),
            html.Script(src="/assets/controllerinputs.js"),
            dcc.Loading(
                html.Div(
                    id={
                        "type": "type-appcore-loading",
                        "index": "index-appcore-loading",
                    },
                    className="",
                ),
                fullscreen=True,
                type="circle",
                style={"backgroundColor": "#0f253700"},
            ),
            html.Div(
                [],
                id="appcore-container",
            ),
        ],
        id="main",
    )
