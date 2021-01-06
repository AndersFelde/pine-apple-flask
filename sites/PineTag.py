from flask import Blueprint, render_template
tag = Blueprint("tag", __name__, template_folder="templates",
                static_folder="static")


@tag.route("/PineTag")
def page():
    return render_template("PineTag.html")
