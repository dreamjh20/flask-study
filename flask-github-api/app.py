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
    commit_url = f'https://github-readme-stats.vercel.app/api?username={user_name}'
    print(commit_url)
    response = requests.get(url).json()
    print(response)
    follower = response['followers']
    print(follower)
    following = response['following']
    print(following)

    # html = urlopen(commit_url)
    # print('11111')
    # bsObject = BeautifulSoup(html, "html.parser")
    # print('22222')
    # commit_count = bsObject.select('class="stat"')
    # print(commit_count)

    # html = response.text
    # bsObject = BeautifulSoup(html, 'html.parser')

    # print('------COMMIT__1------')
    # res = requests.get(commit_url)
    # res.raise_for_status()
    # bsObject = BeautifulSoup(commit_url, "html.parser")
    # print('------COMMIT__2------')
    # print(bsObject.text)
    # print(len(bsObject.find_all(class_="stat")))

    return 'INFO'


@app.route('/firstcommit', methods=['GET'])
def first_commit():
    
    if request.args.get("username") is not None:
        user_name=  request.args.get("username")
    if request.args.get("repository") is not None:
        user_repository=  request.args.get("repository")
    
    url = f'https://api.github.com/repos/{user_name}/{user_repository}/commits'
    response = requests.get(url).json()
    print('1111111')
    print('2222222')

    print(user_name)
    print(user_repository)
    return "FC"

if __name__ == "__main__":
    app.run()
