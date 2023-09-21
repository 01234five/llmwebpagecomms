from dash.dependencies import Input, Output, State, ALL
from dash import no_update


def RegisterCallback(_app):
    @_app.callback(
        Output("id-appaichat-button-send", "className", allow_duplicate=True),
        Input("id-appaichat-input", "value"),
        prevent_initial_call=True,
    )
    def update_textarea_style(text):
        if text == None:
            return no_update
        button_style = "fa-solid fa-paper-plane appaichat-button-send"
        text_length = len(text)
        if text_length > 0:
            button_style = "fa-solid fa-paper-plane appaichat-button-send appaichat-button-send-active"
        return button_style
