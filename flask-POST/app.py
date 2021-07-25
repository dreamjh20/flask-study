from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/post",methods=['POST'])
def post():
	value = request.form['input']
	msg = "%s 어서와~" %value
	return render_template('welcome.html', value = msg)

if __name__ == "__main__":
		app.run(host='10.156.146.106')