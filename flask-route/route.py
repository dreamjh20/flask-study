from flask import Flask
app = Flask(__name__)

@app.route('/')
def Notion():
    return "<h1>Main</h1>"

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile :' + username

if __name__ == "__main__":
    app.run()