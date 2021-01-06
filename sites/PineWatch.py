from flask import Blueprint, render_template
watch = Blueprint("watch", __name__, template_folder="templates",
                  static_folder="static")


@watch.route("/PineWatch")
def page():
    return render_template("PineWatch.html")
