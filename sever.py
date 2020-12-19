from flask import Flask
from flask import render_template

import os
from templates import API_creator as api

app = Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/use')
def home():
    return str("123")


app.run()
