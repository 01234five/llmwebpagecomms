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
                                            html.P(
                                                "AI Chat v1.0",
                                                className="appaichat-message-text",
                                            ),
                                        ],
                                        className="appaichat-message-text-container appaichat-text-title",
                                    ),
                                ],
                                className="appaichat-message-group-container",
                            ),
                        ],
                        className="appaichat-message-group appaichat-message-color-b",
                    ),
                ],
                className="appaichat-messagegroup-list",
                id="id-appaichat-messagegroup-list",
            ),
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
            ),
        ],
        id="appaichat-container",
    )
