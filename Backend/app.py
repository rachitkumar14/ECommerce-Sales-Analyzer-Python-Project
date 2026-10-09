from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/home",methods=["GET"])
def home():
    return jsonify({"rachit":"My name is Rachit"})

if __name__ == "__main__":
    app.run(debug=True)