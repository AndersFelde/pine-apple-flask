from flask import Blueprint, render_template
phone = Blueprint("phone", __name__, template_folder="templates",
                 static_folder="static")


@phone.route("/PinePhone")
def page():
    return render_template("PinePhone.html")
