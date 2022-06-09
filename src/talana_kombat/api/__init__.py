"""API blueprint configuration."""
from flask import Blueprint
from flask_restx import Api


from talana_kombat.api.kombat.endpoints import kombat_ns


"""Base blueprint"""
api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    api_bp,
    version="1.0",
    title="Flask API for Talana Kombat App!",
    description="Swagger UI Documentation",
    doc="/ui",
    authorizations=None
)

api.add_namespace(kombat_ns, path="/kombat")