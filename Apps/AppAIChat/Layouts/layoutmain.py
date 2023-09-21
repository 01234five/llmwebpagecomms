from dash import html, dcc
import Apps.AppAIChat.Layouts.layout as layoutaichat
import Apps.AppAIChat.Layouts.layoutside as layoutside


def Render():
    return html.Div(
        [
            layoutside.Render(),
            html.Button(
                className="btn btn-primary appaichat-button-togglechat fa-solid fa-arrow-right-arrow-left",
                id="appaichat-button-togglechat",
            ),
            layoutaichat.Render(),
        ],
        id="appaichatmain-container",
    )
