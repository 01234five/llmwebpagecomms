import requests
from dash.dependencies import Input, Output, State, ALL
from dash import no_update, html
import Apps.AppAIChat.Components.ChatText as ChatText
from dash import callback_context as ctx


def RegisterCallback(_app):
    @_app.callback(
        Output("appaichat-container", "className", allow_duplicate=True),
        Output("id-appaichat-fixed-bottom", "className", allow_duplicate=True),
        Input("appaichat-button-togglechat", "n_clicks"),
        Input("appaichat-button-close", "n_clicks"),
        State("appaichat-container", "className"),
        prevent_initial_call=True,
    )
    def OnClick(clicks, clicks_btnclose, cn):
        if ctx.triggered:
            trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
            if trigger_id == "appaichat-button-togglechat":
                if clicks == None:
                    return no_update
                if clicks > 0:
                    if cn == "appaichat-container appaichat-show" or cn == None:
                        return (
                            "appaichat-container appaichat-hide",
                            "appaichat-message-group appaichat-fixed-bottom appaichat-fixed-bottom-hide",
                        )
                    else:
                        return (
                            "appaichat-container appaichat-show",
                            "appaichat-message-group appaichat-fixed-bottom",
                        )
            elif trigger_id == "appaichat-button-close":
                if clicks_btnclose == None:
                    return no_update
                if clicks_btnclose > 0:
                    if cn == "appaichat-container appaichat-show" or cn == None:
                        return (
                            "appaichat-container appaichat-hide",
                            "appaichat-message-group appaichat-fixed-bottom appaichat-fixed-bottom-hide",
                        )
                    else:
                        return (
                            "appaichat-container appaichat-show",
                            "appaichat-message-group appaichat-fixed-bottom",
                        )
        return no_update, no_update
