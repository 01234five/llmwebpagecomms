from dash import Dash
from flask import session
from flask import Flask
import HttpGetRequests as HttpGetRequests
from flask_session import Session
import dash_bootstrap_components as dbc
from Apps.AppCore.Layouts.layout import Render as layout
import Apps.AppCore.Callbacks.CallbackController as callback_controller
import Apps.AppAIChat.Callbacks.CallbackAIChatInput as callback_aichat_input
import Apps.AppAIChat.Callbacks.CallbackAIChatButtonSend as callback_aichat_buttonsend
import Apps.AppAIChat.Callbacks.CallbackAIChatAPICall as callback_aichat_apicall

# Configure session handling
server = Flask(__name__)
server.config["SECRET_KEY"] = "my-secret-key"  # We need to decide on a secret key
server.config["SESSION_TYPE"] = "filesystem"  # Use filesystem-based session storage
server.config["PERMANENT_SESSION_LIFETIME"] = 604800  # 1 week in seconds

# Initialize session object with configuration above
Session(server)

app = Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
    prevent_initial_callbacks="initial_duplicate",
    external_stylesheets=[
        dbc.themes.SUPERHERO,
        dbc.icons.FONT_AWESOME,
    ],
)
app.layout = layout

# Custom attributes assignments to app object
app.serversession = session
server = app.server

HttpGetRequests.RegisterGetRequests(app.server)
# App Callbacks----------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
callback_controller.RegisterCallback(app, app.serversession)
callback_aichat_input.RegisterCallback(app)
callback_aichat_buttonsend.RegisterCallback(app)
callback_aichat_apicall.RegisterCallback(app)


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=False)
