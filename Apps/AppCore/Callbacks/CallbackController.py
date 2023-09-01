from dash import Input, State, Output, html, ctx, no_update
import Apps.AppAIChat.Layouts.layout as layout


def RegisterCallback(_app, session):
    # create a callback to display the pages
    @_app.callback(
        Output("appcore-container", "children"),
        Input("url", "pathname"),
    )
    def render_page_content(pathname):
        if pathname in ["/aichat"]:
            return [
                layout.Render(),
            ]
        else:
            return html.Div("Error 404: Not Found")
