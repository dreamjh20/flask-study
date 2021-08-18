from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods = ['POST'])
def setcookie():
    if request.method == 'POST':
        user_name = request.form['name']

    user_name = str(user_name)
    Myresponse = make_response(user_name)
    print(Myresponse)
    Myresponse.set_cookie('userName', user_name)
    print(user_name)
    return render_template('setcookie.html', value = Myresponse)

@app.route('/getcookie')
def getcookie():
    Myname = request.cookies.get('userName')
    return '<h1>' + Myname + '</h1>'
    
if __name__ == "__main__":
		app.run()