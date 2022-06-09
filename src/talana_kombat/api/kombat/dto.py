"""Data Transfer Objects for the Kombat API"""
from flask_restx import Model
from flask_restx.reqparse import RequestParser
from flask_restx.fields import Nested, String, List


kombat_reqparser = RequestParser(bundle_errors=True)
kombat_reqparser.add_argument(
    name="player1", type=dict, location="json", required=True, nullable=False
)
kombat_reqparser.add_argument(
    name="player2", type=dict, location="json", required=True, nullable=False
)

player1_reqparser = RequestParser(bundle_errors=True)
player1_reqparser.add_argument(
    name="movimientos",
    type=str,
    action="append",
    location=("player1", ),
    required=True,
    nullable=False
)
player1_reqparser.add_argument(
    name="golpes",
    type=str,
    action="append",
    location=("player1", ),
    required=True,
    nullable=False
)

player2_reqparser = RequestParser(bundle_errors=True)
player2_reqparser.add_argument(
    name="movimientos",
    type=str,
    action="append",
    location=("player2", ),
    required=True,
    nullable=False
)
player2_reqparser.add_argument(
    name="golpes",
    type=str,
    action="append",
    location=("player2", ),
    required=True,
    nullable=False
)


player_fields = {}
player_fields["movimientos"] = List(String, attribute="movimientos")
player_fields["golpes"] = List(String, attribute="golpes")

fields_model = Model("fields", player_fields)

player_model = Model(
    "Payload",
    {
        "player1": Nested(fields_model),
        "player2": Nested(fields_model)
    }
)

response_model = Model(
    "response",
    {
        "relato": List(String, attribute="relato")
    }
)
