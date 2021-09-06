import re
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
    github_url = f'https://github.com/{user_name}'

    response = requests.get(url).json()
    print(response)
    follower = response['followers']
    print(follower)
    following = response['following']
    print(following)

    html = urlopen(github_url)
    bsObject = BeautifulSoup(html, "html.parser")

    print(bsObject.head.title)
    commit_count = bsObject.find('h2',class_='f4 text-normal mb-2')
    commit = commit_count.get_text()
    commit = commit[0:-50]
    print(commit)

    profile_image = bsObject.find('img', class_='avatar avatar-user width-full border color-bg-primary')

    return 'INFO'

@app.route('/firstcommit', methods=['GET'])
def first_commit():
    
    if request.args.get("username") is not None:
        user_name=  request.args.get("username")
    if request.args.get("repository") is not None:
        user_repository=  request.args.get("repository")
    
    url = f'https://api.github.com/repos/{user_name}/{user_repository}/commits?per_page=1'
    print('1111111')
    response = requests.get(url).json()
    print(response)
    
    print('2222222')

    print(user_name)
    print(user_repository)
    return "FC"

if __name__ == "__main__":
    app.run()
