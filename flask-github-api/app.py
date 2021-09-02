from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    print('HOME')
    return render_template('home.html')

@app.route('/result', methods=['GET'])
def get_info():
    if request.args.get("username") is not None:
        user_name=  request.args.get("username")
    if request.args.get("username") is not None:
        my_repository=  request.args.get("repository")
    return (my_repository)

if __name__ == "__main__":
    app.run()
