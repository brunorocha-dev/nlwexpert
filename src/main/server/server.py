from flask import Flask
from src.main.routes.tag_routes import tags_routes_bp

app = Flask(__name__)
# Registrar todas as blueprints
app.register_blueprint(tags_routes_bp)
