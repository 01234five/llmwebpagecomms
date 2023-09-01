import os
from flask import send_from_directory


def RegisterGetRequests(server):
    """
    @server.route("/dmap/lottie/loader-1", methods=["GET"])
    def serving_lottie_loader_1():
        directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "assets/survey"
        )
        return send_from_directory(directory, "survey_complete.json")

    @server.route("/dmap/teamlottie/loader-1", methods=["GET"])
    def teamapp_serving_lottie_loader_1():
        directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/assetsappteam/assets/lottie",
        )
        return send_from_directory(directory, "feedback-analysis.json")

    @server.route("/dmap/teamlottie/loader-2", methods=["GET"])
    def teamapp_serving_lottie_loader_2():
        directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/assetsappteam/assets/lottie",
        )
        return send_from_directory(directory, "project-management.json")

    @server.route("/dmap/teamlottie/loader-3", methods=["GET"])
    def teamapp_serving_lottie_loader_3():
        directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets/assetsappteam/assets/lottie",
        )
        return send_from_directory(directory, "about-our-teamwork.json")
        """