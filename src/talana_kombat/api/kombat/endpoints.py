"""Endpoint definitions for kombat namespace"""
from http import HTTPStatus
from http.client import OK

from flask_restx import Namespace, Resource

kombat_ns = Namespace(name="kombat", validate=True)


@kombat_ns.route("/start", endpoint="kombat_start")
class StartKombat(Resource):
    """Handles HTTP requests to URL: /api/v1/kombat/start."""

    @kombat_ns.response(int(HTTPStatus.ACCEPTED), "Kombat as begun!")
    @kombat_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @kombat_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR),
                        "Internal server error.")
    def post(self):
        """Fight!"""
        return OK
