from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
import csv
@app.route("/", methods=["GET", "POST"])
def index2():

	if request.method == "POST":
		sort = request.form["sort"]
		listsort = sort.split(",")
		listsort = [int(i) for i in listsort]
		isSorted = 0  # We haven't started sorting yet

		with open('bubble.csv','w') as csv_out:
			writer = csv.writer(csv_out)				
			writer.writerow(listsort)

		while isSorted == 0:
			isSorted = 1  # Assume the list is now sorted
			for element in range(0, len(listsort)-1):
				if int(listsort[element]) > int(listsort[element + 1]):
					isSorted = False  # We found two elements in the wrong order
					hold = (listsort[element + 1])
					(listsort[element + 1]) = (listsort[element])
					listsort[element] = hold
					with open('bubble.csv','a') as csv_out:
						writer = csv.writer(csv_out)				
						writer.writerow(listsort)	
		return redirect(url_for("Sorted"))			

	return render_template("index2.html")
	
@app.route("/Sorted")
def Sorted():

    with open('bubble.csv','r') as csv_in:
        reader = csv.reader(csv_in)
        return render_template("sorted.html", dispList=reader)
		
