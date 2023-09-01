from dash.dependencies import Input, Output, State, ALL
from dash import no_update


def RegisterCallback(_app):
    @_app.callback(
        Output("id-appaichat-button-send", "style", allow_duplicate=True),
        Input("id-appaichat-input", "value"),
        prevent_initial_call=True,
    )
    def update_textarea_style(text):
        if text == None:
            return no_update
        button_style = {}
        text_length = len(text)
        if text_length > 0:
            button_style = {"backgroundColor": "#19C37D"}
        return button_style
