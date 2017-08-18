# Import Flask Library
from flask import Flask

# create a Flask application instance
app = Flask(__name__)

# define a route through the app.route decorator
@app.route("/")
def index():
    return "<h1>Hot Food!</h1>"
    
# launch the integrated development web server
# and run the app on http://localhost:8085
if __name__=="__main__":
   app.run(debug=True,port=8086)
   
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
