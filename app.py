from flask import Flask,render_template
from elasticsearch import Elasticsearch


app=Flask(__name__)
client = Elasticsearch("http://localhost:9200")

@app.route('/')
def index():
    mappings = {
        "properties": {
            "foo": {"type": "text"},
            "bar": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256,
                    }
                },
            },
        }
    }
    client.indices.create(index="my_index", mappings=mappings)
    client.index(
        index="my_index",
        id="my_document_id",
        document={
            "foo": "foo",
            "bar": "bar",
        },
    )
    client.update(
    index="my_index",
    id="my_document_id",
    doc={
        "foo": "bar",
        "new_field": "new value",
    },
)
    f=client.get(index="my_index", id="my_document_id")


    return render_template('index.html',messages=f)