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
    Myresponse.set_cookie('UserName', user_name)
    print(user_name)
    return render_template('setcookie.html', value = Myresponse)

@app.route('/getcookie')
def getcookie():
    print("1111111111111111111111111")
    MyName = request.cookies.get('UserName')
    print('2222222222222222222222222')
    print(MyName)

    return '<h1>' + MyName + '</h1>'

if __name__ == "__main__":
		app.run()