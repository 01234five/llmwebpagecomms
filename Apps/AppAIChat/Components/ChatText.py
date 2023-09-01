from dash import html, dcc


def Render(_icon, _text, _classType="a"):
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [],
                                className="appaichat-message-icon-"
                                + _classType
                                + " "
                                + _icon,
                            ),
                        ],
                        className="appaichat-message-icon-container",
                    ),
                    html.Div(
                        [
                            html.Pre(
                                _text,
                                className="appaichat-message-text",
                            ),
                        ],
                        className="appaichat-message-text-container",
                    ),
                ],
                className="appaichat-message-group-container",
            ),
        ],
        className="appaichat-message-group appaichat-message-color-" + _classType,
    )
