from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/post",methods=['POST'])
def post():
	value = request.form['input']
	msg = "%s 어서 와~" %value
	print(value)
	return render_template('welcome.html', value = msg)

if __name__ == "__main__":
		app.run(host='192.168.137.241')