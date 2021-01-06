from flask import Flask, render_template, request
from sites.home import home
from sites.PinePhone import phone
from sites.PinePad import pad
from sites.PineTag import tag
from sites.PineWatch import watch
from sites.ThePineApple import pineApple

site = Flask(__name__)
site.register_blueprint(home)
site.register_blueprint(phone)
site.register_blueprint(pad)
site.register_blueprint(tag)
site.register_blueprint(watch)
site.register_blueprint(pineApple)


if __name__ == "__main__":
    site.run(debug=True)
