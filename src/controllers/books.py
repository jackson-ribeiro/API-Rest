from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.models.books import book

app, api = server.app, server.api

books = [
    {"id": 0, "title": "War and Peace"},
    {"id": 1, "title": "Clean Code"},
    {"id": 2, "title": "The Lord of the Rings"},
]


@api.route("/books")
class BookList(Resource):
    @api.marshal_list_with(book)
    def get(
        self,
    ):
        return books

    @api.expect(book, validate=True)
    @api.marshal_with(book)
    def post(
        self,
    ):
        response = api.payload
        books.append(response)
        return response, 200
