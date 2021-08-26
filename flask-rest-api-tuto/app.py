from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/language/<language>')
def environments(language):
    return jsonify({"language":language})

if __name__ == "__main__":
    app.run()
