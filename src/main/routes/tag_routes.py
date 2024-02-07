from flask import Blueprint, request, jsonify

# biblioteca para normear todas as rotas de tag para saber as responsabilidades
tags_routes_bp = Blueprint("tags_route", __name__)
# para cada rota que eu criar vou adicionar um decorador Blueprint
@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tag():
    print(request.json)  # O body da requisição http
    return jsonify({"resposta": "ok"}), 200
