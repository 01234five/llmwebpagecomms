import requests
from dash.dependencies import Input, Output, State, ALL
from dash import no_update, html
import Apps.AppAIChat.Components.ChatText as ChatText


def RegisterCallback(_app):
    @_app.callback(
        Output("id-appaichat-messagegroup-list", "children", allow_duplicate=True),
        Output(
            {
                "type": "type-appcore-loading",
                "index": "index-appcore-loading",
            },
            "className",
            allow_duplicate=True,
        ),
        Input("id-appaichat-messagegroup-list", "children"),
        prevent_initial_call=True,
    )
    def OnChange(dom_elements):
        if dom_elements is not None and len(dom_elements) > 0:
            lastindex_classname = dom_elements[-1]["props"]["className"]
            if (
                lastindex_classname
                == "appaichat-message-group appaichat-message-color-a"
            ):
                lastindex_message = dom_elements[-1]["props"]["children"][0]["props"][
                    "children"
                ][1]["props"]["children"][0]["props"]["children"]
                url = "http://127.0.0.1:5110/api/prompt"
                params = {"prompt_user": lastindex_message}
                response = requests.get(url, params=params)

                # Check the response status code
                if response.status_code == 200:
                    # The request was successful, and you can access the response content
                    data = response.json()  # Assuming the response is in JSON format
                    print(data)
                    dom_elements.append(
                        ChatText.Render("fa-solid fa-robot", data["Answer"], "b"),
                    )
                    return dom_elements, no_update
                else:
                    # The request encountered an error
                    print(f"Error: {response.status_code}")
                    dom_elements.append(
                        ChatText.Render(
                            "fa-solid fa-robot",
                            "Error, try again or contact administrator.",
                            "b",
                        ),
                    )
                    return dom_elements, no_update

        return no_update, no_update
