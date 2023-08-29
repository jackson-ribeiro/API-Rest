from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

books = [
    {"id": 0, "title": "War and Peace"},
    {"id": 1, "title": "Clean Code"},
    {"id": 2, "title": "The Lord of the Rings"},
]


@api.route("/books")
class BookList(Resource):
    def get(
        self,
    ):
        return books

    def post(
        self,
    ):
        response = api.payload
        books.append(response)
        return response, 200
