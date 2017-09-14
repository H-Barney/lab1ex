from flask import Flask, redirect, render_template, request, url_for
from server import app, calc_string
from math import sin, cos, tan, sqrt, log
import ast

@app.route("/", methods=["GET", "POST"])
def index():
	global calc_string
	if request.method == "POST":
		calc = request.form["bt"]
		if calc == "=":
			calc_string = str(eval(calc_string))
		elif calc == "C":
			if calc_string.rfind("n") == len(calc_string)-1:
			 	calc_string = calc_string[:-3]
			elif calc_string.rfind("s") == len(calc_string)-1:
			 	calc_string = calc_string[:-3]
			elif calc_string.rfind("t") == len(calc_string)-1:
				calc_string = calc_string[:-4]
			elif calc_string.rfind("g") == len(calc_string)-1:
				 calc_string = calc_string[:-3]
			else:
				calc_string = calc_string[:-1]
		elif calc == "CE":
			calc_string = ""
		else:
			calc_string+=calc
				

	return render_template("index.html", button=calc_string)
	

