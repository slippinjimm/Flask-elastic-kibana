from flask import Flask
from elasticsearch import Elasticsearch


app=Flask(__name__)
client = Elasticsearch("http://localhost:9200")

from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "days_of_week": [
        {"id": 1, "name": "Понедельник"},
        {"id": 2, "name": "Вторник"},
        {"id": 3, "name": "Среда"},
        {"id": 4, "name": "Четверг"},
        {"id": 5, "name": "Пятница"},
        {"id": 6, "name": "Суббота"},
        {"id": 7, "name": "Воскресенье"},
    ]
}



@app.route('/', methods=['GET'])
def get_users():
    return jsonify(data["days_of_week"])



if __name__ == '__main__':
    app.run()