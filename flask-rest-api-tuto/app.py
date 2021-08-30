from flask import Flask, request, jsonify
from flask.templating import render_template
app = Flask(__name__)

@app.route('/moon')
def moon():
    return jsonify({"message":"i'm moon"})



@app.route('/language/<language>')
def environments(language):
    return jsonify({"language":language})

@app.route("/", methods=['GET'])
def get_language():
    if request.args.get("language") is not None:
        lang=request.args.get("language")
        print(lang)
    else:
        lang = "Default"
    return render_template('index.html', v_lang=lang)

if __name__ == "__main__":
    app.run()
