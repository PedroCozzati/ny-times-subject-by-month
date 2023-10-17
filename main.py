# app.py

from flask import Flask, render_template, request

from flask import render_template # Remove: import Flask
import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/api/subjects")
# def read_all():
    
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)