from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/subscribe", methods=["POST"])
def subscribe():
  name = request.form["name"]
  gf_name = request.form["gf_name"]
  email = request.form["email"]
  key = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
  tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+email+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+key
  requests.get("https://wa.me/+923344706269?text=" + tks)
  return "Subscription successful!"

if __name__ == "__main__":
  app.run()
