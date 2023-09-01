import requests
from dash.dependencies import Input, Output, State, ALL
from dash import no_update, html
import Apps.AppAIChat.Components.ChatText as ChatText


def RegisterCallback(_app):
    @_app.callback(
        Output("id-appaichat-messagegroup-list", "children", allow_duplicate=True),
        Output("id-appaichat-input", "value", allow_duplicate=True),
        Input("id-appaichat-button-send", "n_clicks"),
        State("id-appaichat-messagegroup-list", "children"),
        State("id-appaichat-input", "value"),
        prevent_initial_call=True,
    )
    def OnClick(clicks, dom_elements, _text):
        if clicks == None:
            return no_update, no_update
        if clicks > 0:
            if not _text.strip():
                dom_elements.append(
                    ChatText.Render("fa-solid fa-user", _text, "a"),
                )
                dom_elements.append(
                    ChatText.Render(
                        "fa-solid fa-robot",
                        "It seems like your message is empty. If you have any more questions or need further assistance, please feel free to ask!",
                        "b",
                    ),
                )
                return dom_elements, ""
            if not _text == "":
                dom_elements.append(
                    ChatText.Render("fa-solid fa-user", _text, "a"),
                )
                return dom_elements, ""
            else:
                return no_update, ""
