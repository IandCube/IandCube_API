from flask import Flask
from flask import render_template
from flask_cors import CORS

import os
from myproject import API_creator as api


app = Flask(__name__)
CORS(app)
# app.config["DEBUG"] = True


@app.route('/')
def home():
    return ("<p>home</p>")


@app.route('/page2_1_b_a')
def page2_1_b_a():
    return (api.page2_1_b_a())


@app.route('/page2_1_b_b')
def page2_1_b_b():
    return (api.page2_1_b_b())


@app.route('/page2_1_b_c')
def page2_1_b_c():
    return (api.page2_1_b_c())


# @app.route('/demo4')
# def demo4():
#     return (api.demo4())


# @app.route('/demo5')
# def demo5():
#     return (api.demo5())


if __name__ == "__main__":
    app.run()
    # print(api.demo3())
