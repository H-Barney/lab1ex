from flask import Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "Highly secret key"

calc_string = str()
