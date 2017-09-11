import os
from flask import Flask, render_template, request, redirect, session, flash, url_for
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
	if len(request.form["name"]) < 1:
		flash("Must enter a name")
		return redirect("/")
	else:	
		session["name"] = request.form["name"]
	session["location"] = request.form["location"]
	session["language"] = request.form["language"]
	if len(request.form["comment"]) < 1:
		flash("Must enter a comment")
		return redirect("/")
	elif len(request.form["comment"]) > 120:
		flash("Comment must be 120 characters or fewer")
		return redirect("/")
	else:
		session["comment"] = request.form["comment"]
	return redirect("/result")

@app.route("/result")
def result():
	return render_template("result.html",name=session["name"],location=session["location"],language=session["language"],comment=session["comment"])

@app.route("/back")
def back():
	return redirect("/")

app.run(debug=True)