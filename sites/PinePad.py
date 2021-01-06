from flask import Blueprint, render_template
pad = Blueprint("pad", __name__, template_folder="templates",
                static_folder="static")


@pad.route("/PinePad")
def page():
    return render_template("PinePad.html")
