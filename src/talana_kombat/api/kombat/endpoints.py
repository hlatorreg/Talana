"""Endpoint definitions for kombat namespace"""
from http import HTTPStatus
from http.client import OK

from flask_restx import Namespace, Resource

from talana_kombat.api.kombat.business import get_relato

from talana_kombat.api.kombat.dto import (
    fields_model,
    player_model,
    response_model,
    kombat_reqparser,
    player1_reqparser,
    player2_reqparser
)

kombat_ns = Namespace(name="kombat", validate=True)
kombat_ns.models[fields_model.name] = fields_model
kombat_ns.models[player_model.name] = player_model
kombat_ns.models[response_model.name] = response_model


@kombat_ns.route("/start", endpoint="kombat_start")
class StartKombat(Resource):
    """Handles HTTP requests to URL: /api/v1/kombat/start."""

    @kombat_ns.expect(kombat_reqparser)
    # @kombat_ns.marshal_with(player_model)
    @kombat_ns.response(int(HTTPStatus.OK), "Kombat as begun!", response_model)
    @kombat_ns.response(int(HTTPStatus.BAD_REQUEST), "Validation error.")
    @kombat_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR),
                        "Internal server error.")
    def post(self):
        """Fight!"""
        fight_args = kombat_reqparser.parse_args()
        player1_reqparser.parse_args(req=fight_args)
        player2_reqparser.parse_args(req=fight_args)
        return get_relato(fight_args), OK
