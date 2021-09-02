from flask import Flask, render_template, request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json


app = Flask(__name__)

@app.route('/')
def home():

    print('HOME')
    return render_template('home.html')

@app.route('/result', methods=['GET'])
def get_info():
    if request.args.get("username") is not None:
        user_name=  request.args.get("username")
    print(user_name)
    url=f'https://api.github.com/users/{user_name}'
    url2 = f'https://api.github.com/repos/dreamjh20/embedded/commits'
    
    response = requests.get(url).json()
   
    print(response)
    follower = response['followers']
    following = response['following']
    return 'INFO'

if __name__ == "__main__":
    app.run()
