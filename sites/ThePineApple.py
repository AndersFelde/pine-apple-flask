from flask import Blueprint, render_template
pineApple = Blueprint("pineApple", __name__, template_folder="templates",
                      static_folder="static")


@pineApple.route("/ThePineApple")
def page():
    return render_template("ThePineApple.html")
