from flask import Flask
from flask import render_template

import os
from myproject import API_creator as api

app = Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/')
def home():
    return ("<p>home</p>")

@app.route('/test')
def test():
    return ("<p>test</p>")

if __name__=="__main__":
    app.run()
