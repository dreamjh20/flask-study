from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['myfile']
        f.save(secure_filename(f.filename))
        return 'SUCCEED'

if __name__ == '__main__':
    app.run(debug=True)