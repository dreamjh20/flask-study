from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

imgFolder = os.path.join('static', 'image')

app.config['UPLOAD_FOLDER'] = imgFolder

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['myfile']  #파일 받아오기
        f.save('./static/image/' + secure_filename(f.filename)) #파일 경로 설정 + 암호화
        #print(f.filename) #파일 이름 출력
        return_str = f.filename + " SUCCEED"
        return return_str

@app.route('/image') #url 지정
def imgshow():
    image=os.path.join(app.config['UPLOAD_FOLDER'], 'jang.jpg')
    return render_template("imgshow.html", show_image = image)


if __name__ == '__main__':
    app.run(debug=True)