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
    
    response = requests.get(url).json()
    print(response)
    follower = response['followers']
    print(follower)
    following = response['following']
    print(following)
    return 'INFO'


@app.route('/firstcommit', methods=['GET'])
def first_commit():
    
    if request.args.get("username") is not None:
        user_name=  request.args.get("username")
    if request.args.get("repository") is not None:
        user_repository=  request.args.get("repository")
    
    url = f'https://api.github.com/repos/{user_name}/{user_repository}/commits'
    response = requests.get(url).json()
    print('111111')
    print('222222')

    print(user_name)
    print(user_repository)
    return "FC"

if __name__ == "__main__":
    app.run()
