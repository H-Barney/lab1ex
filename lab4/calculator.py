from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
import csv
@app.route("/", methods=["GET", "POST"])
def index():

	if request.method == "POST":
		pass
				

	return render_template("index.html")
	

