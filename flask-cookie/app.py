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
    Myresponse = make_response(render_template('setcookie.html'))
    print(Myresponse)
    Myresponse.set_cookie('UserName', user_name)
    print(user_name)
    return Myresponse

@app.route('/getcookie')
def getcookie():
    MyName = request.cookies.get('UserName')
    print(MyName)

    return '<h1>' + MyName + '</h1>'

if __name__ == "__main__":
		app.run()