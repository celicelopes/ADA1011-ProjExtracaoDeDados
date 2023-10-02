import flask
from connectNewsAPI import connectNewsApi
from saveData import saveData


app = flask.Flask(__name__)

@app.route("/updateNews", methods=["GET"])
def handle_webhook():
    data = connectNewsApi()
    saveData(data)
    
    return "OK"

if __name__ == "__main__":
    app.run()