import flask
from connectNewsAPI import connectNewsApi
from saveData import saveData
from treatData import count_articles_by_date

app = flask.Flask(__name__)

@app.route("/updateNews", methods=["GET"])
def handle_webhook():
    data = connectNewsApi()
    saveData(data)

    return "OK"

@app.route("/byDate")
def handle_by_date():
    count_by_year, count_by_month, count_by_day = count_articles_by_date("./data/data.parquet")

    print("Count by Year:")
    print(count_by_year)

    print("\nCount by Month:")
    print(count_by_month)

    print("\nCount by Day:")
    print(count_by_day)
    return "Data treated"


if __name__ == "__main__":
    app.run()
