from flask import Flask, request, jsonify, make_response
import json

app = Flask (__name__)

tasks = [
    {
        'id': 1,
        'name': "Produto 1",
        "description": "Esse é o produto 1"
    },
    {
        "id": 2,
        "name": 'Produto 2',
        "description": "Esse é o produto 2"
    },
    {
         "id": 3,
        "name": 'Produto 3',
        "description": "Esse é o produto 3"
    }
]

Lista_de_produtos = json.dumps(tasks)

class Model():
    def produtos():
        #comunicação banco
        #regra de negocios
        return Lista_de_produtos
