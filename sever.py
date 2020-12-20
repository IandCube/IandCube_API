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
    return ("")


@app.route('/英檢報名表')
def test():
    return (api.value())


if __name__ == "__main__":
    app.run()

    # print(api.value())
