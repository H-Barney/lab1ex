from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
import csv
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        zID = int(request.form["zID"])
        description = request.form["desc"]
        
        with open('example.csv','a') as csv_out:
            writer = csv.writer(csv_out)
            writer.writerow([name, zID, description])

        return redirect(url_for("hello"))
    return render_template("index.html")

@app.route("/Hello")
def hello():

    with open('example.csv','r') as csv_in:
        reader = csv.reader(csv_in)
        for row in reader:
        	return render_template("hello.html", all_users=reader)
   
#
#
#
#
#
#
#@app.route('/',methods=['GET', 'POST'])
#def index():
#if request.method = 'POST'
#	name = request.form['name']
#	zid = int(request.form['zid']
#	desc = reqiest.form['desc']
#	return redirect(url_for('hello, name=myname, zid=zid, desc=desc))
#return render_template('index.html')
#
#
#
#@app.route('/hello/<name>/,<zid>/<desc>')
#def hello(name,zid,desc):
#	return render_template('hello.html', users=user_input)
