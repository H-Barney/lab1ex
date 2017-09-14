from flask import Flask, redirect, render_template, request, url_for
from wtforms import Form, BooleanField, StringField, validators
from server import app, user_input
from classes2 import Question
import csv

@app.route("/", methods=["GET", "POST"])
def index():

	if request.method == "POST":
	
		if request.form["bt"] == "question":
			return redirect(url_for("question_add"))
		#if request.form == "AddSurvey":
			#return redirect(url_for(""))
	
	return render_template("index.html")


@app.route("/questionAdd", methods=["GET", "POST"])
def question_add():

	if request.method == "POST":
	
		question = request.form["question"]
		response = [request.form["responseA"]]
		addQuestion = Question(question,response)
		addQuestion.add_question(question,response)
					

	return render_template("question_add.html")
