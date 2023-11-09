# app.py

from flask import Flask, render_template, request

from flask import render_template # Remove: import Flask

from subjects import read_all

# app = connexion.App(__name__, specification_dir="./")
# app.add_api("swagger.yml")

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("home.html")

@app.route("/subjects",methods=["GET"])
def subjects():
    return read_all()
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)