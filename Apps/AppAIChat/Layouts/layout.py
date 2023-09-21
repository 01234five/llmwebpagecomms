from dash import html, dcc
import Apps.AppAIChat.Components.ChatText as ChatText


def Render():
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(style={"marginLeft": "10px"}),
                                            html.P(
                                                "AI Chat v1.0",
                                                className="appaichat-message-text",
                                                style={"margin": "0px"},
                                            ),
                                            html.Button(
                                                className="btn btn-close",
                                                style={"marginRight": "10px"},
                                                id="appaichat-button-close",
                                            ),
                                        ],
                                        className="appaichat-message-text-container appaichat-text-title",
                                        style={"paddingLeft": "0px"},
                                    ),
                                ],
                                className="appaichat-message-group-container",
                                style={"height": "100%", "maxWidth": "unset"},
                            ),
                        ],
                        className="appaichat-message-group appaichat-message-color-b",
                        style={"height": "88.8px"},
                    ),
                ],
                className="appaichat-messagegroup-list",
                id="id-appaichat-messagegroup-list",
            ),
            html.Div(className="appaichat-whitespace"),
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Textarea(
                                        id="id-appaichat-input",
                                        placeholder="Send Message",
                                        className="appaichat-input",
                                        wrap=True,
                                        draggable=False,
                                        spellCheck=True,
                                    ),
                                    html.Button(
                                        className="fa-solid fa-paper-plane appaichat-button-send",
                                        id="id-appaichat-button-send",
                                    ),
                                ],
                                className="appaichat-input-group",
                                style={"position": "relative"},
                            ),
                        ],
                        className="appaichat-message-group-container ",
                    )
                ],
                className="appaichat-message-group appaichat-fixed-bottom",
                id="id-appaichat-fixed-bottom",
            ),
        ],
        id="appaichat-container",
        className="appaichat-container appaichat-show",
    )
