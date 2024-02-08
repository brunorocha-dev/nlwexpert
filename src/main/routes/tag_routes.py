from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

# biblioteca para normear todas as rotas de tag para saber as responsabilidades
tags_routes_bp = Blueprint("tags_route", __name__)
# para cada rota que eu criar vou adicionar um decorador Blueprint
@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tag():
    tag_creator_view = TagCreatorView()

    http_request = HttpRequest(body=request.json)
    response = tag_creator_view.validate_and_create(http_request)

    return jsonify(response.body), response.status_code
