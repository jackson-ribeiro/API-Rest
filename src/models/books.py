from flask_restx import fields

from src.server.instance import server

book = server.api.model(
    "Book",
    {
        "id": fields.String(description="O ID do registro"),
        "title": fields.String(required=True, description="O título do livro"),
    },
)
