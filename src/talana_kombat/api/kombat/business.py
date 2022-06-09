"""Business logic, or fight choreography"""
import itertools
from typing import Tuple


def get_relato(kombat: dict) -> list:
    """
        Punto de entrada para la generación del reporte
    """
    KOMBAT_CONFIG = {
        "player1": {
            "nombre": "Tonyn",
            "health": 6,
            "apellido": "Stallone",
            "combinaciones": {
                "Taladoken": {"movimientos": "DSD", "strike": "P", "daño": 3},
                "Remuyuken": {"movimientos": "SD", "strike": "K", "daño": 2},
                "Golpe": {"movimientos": "", "strike": "P", "daño": 1},
                "Patada": {"movimientos": "", "strike": "K", "daño": 1},
            }
        },
        "player2": {
            "nombre": "Arnaldor",
            "health": 6,
            "apellido": "Shuatseneguer",
            "combinaciones": {
                "Remuyuken": {"movimientos": "SA", "strike": "K", "daño": 3},
                "Taladoken": {"movimientos": "ASA", "strike": "P", "daño": 2},
                "Golpe": {"movimientos": "", "strike": "P", "daño": 1},
                "Patada": {"movimientos": "", "strike": "K", "daño": 1},
            }
        }
    }

    (p1, p2) = define_first(kombat)
    return generate_fight_report(p1, p2, kombat, KOMBAT_CONFIG)


def define_first(kombat: dict) -> tuple[str, str]:
    """
        Define quien es el primer player
        segun las reglas entregadas
        Devuelve un tuplo con player1, player2
    """
    mov_tony = len(kombat["player1"]["movimientos"])
    gol_tony = len(kombat["player1"]["golpes"])
    mov_arnal = len(kombat["player2"]["movimientos"])
    gol_arnal = len(kombat["player2"]["golpes"])
    comb_tony = mov_tony + gol_tony
    comb_arnal = mov_arnal + gol_arnal
    p1_p2 = ("player1", "player2")
    p2_p1 = ("player2", "player1")

    if comb_tony != comb_arnal:
        return p1_p2 if comb_tony < comb_arnal else p2_p1
    if mov_tony != mov_arnal:
        return p1_p2 if mov_tony < mov_arnal else p2_p1
    if gol_tony != gol_arnal:
        return p1_p2 if gol_tony < gol_arnal else p2_p1
    return p1_p2


def generate_fight_report(p1: str, p2: str, kombat: dict, KOMBAT_CONFIG: dict) -> list:
    """
        Genera el reporte de la pelea en
        base a los movimientos ingresados
        y el orden de los jugadores
    """
    narration = list()

    p1_moves = kombat[p1]
    p2_moves = kombat[p2]

    # Combinamos movimientos y combinaciones en listas de tuplos, por player
    p1_combs = list(itertools.zip_longest(p1_moves["movimientos"],
                    p1_moves["golpes"]))
    p2_combs = list(itertools.zip_longest(p2_moves["movimientos"],
                    p2_moves["golpes"]))

    narration.append(f"El primer movimiento lo realiza {p1}")

    for a in list(itertools.zip_longest(p1_combs, p2_combs)):
        if (a[0] is not None):
            narration.append(generate_move_report(p1, a[0], KOMBAT_CONFIG))
        if (KOMBAT_CONFIG[p2]['health'] <= 0):
            narration.append(f"""{KOMBAT_CONFIG[p1]['nombre']} gana la pelea y \
aun le quedan {KOMBAT_CONFIG[p1]['health']} de energía""")
            break

        if (a[1] is not None):
            narration.append(generate_move_report(p2, a[1], KOMBAT_CONFIG))
        if (KOMBAT_CONFIG[p1]['health'] <= 0):
            narration.append(f"""{KOMBAT_CONFIG[p2]['nombre']} gana la pelea y \
aun le quedan {KOMBAT_CONFIG[p2]['health']} de energía""")
            break

    return narration


def generate_move_report(player: str, set: Tuple, KOMBAT_CONFIG: dict) -> str:
    """
        Retorna un string en base a los movimientos
        y/o golpes que el jugador actual esté
        realizando, ademas se encarga de restar
        puntos de energía a los jugadores
    """
    if (set is None):
        return ""
    player_config = KOMBAT_CONFIG[player]
    player_name = player_config["nombre"]
    player_movimiento = set[0]
    player_golpe = set[1] if set[1] != "" else " "

    player_combinaciones = player_config["combinaciones"]

    movimientos = [m["movimientos"] for m in player_combinaciones.values()]
    golpes = [m["strike"] for m in player_combinaciones.values()]

    for (mov, gol) in zip(movimientos, golpes):
        mov_index_inplayermov = player_movimiento.rfind(mov)

        if (mov_index_inplayermov != -1 and
                mov_index_inplayermov + len(mov) == len(player_movimiento) and
                player_golpe in gol):
            nombre_movimiento = list(player_combinaciones.keys())[0]

            damage = KOMBAT_CONFIG[player]["combinaciones"][nombre_movimiento]["daño"]
            if (player == "player2"):
                KOMBAT_CONFIG["player1"]["health"] -= damage
            else:
                KOMBAT_CONFIG["player2"]["health"] -= damage

            return f"""{player_name} lanza un {nombre_movimiento}, \
{KOMBAT_CONFIG['player1']['nombre']} tiene \
{KOMBAT_CONFIG['player1']['health']} energia, \
{KOMBAT_CONFIG['player2']['nombre']} tiene \
{KOMBAT_CONFIG['player2']['health']} energia"""
        else:
            nombre_movimiento = [m for m, v in player_combinaciones.items()
                                if v["strike"] == player_golpe and
                                v["movimientos"] == ""]

            if len(nombre_movimiento) == 0:
                return f"{player_name} se mueve"

            damage = (KOMBAT_CONFIG[player]["combinaciones"]
                        [nombre_movimiento[0]]
                        ["daño"])

            if (player == "player2"):
                KOMBAT_CONFIG["player1"]["health"] -= damage
            else:
                KOMBAT_CONFIG["player2"]["health"] -= damage

            return f"""{player_name} se mueve y lanza un {nombre_movimiento[0]}, \
{KOMBAT_CONFIG['player1']['nombre']} tiene \
{KOMBAT_CONFIG['player1']['health']} energia, \
{KOMBAT_CONFIG['player2']['nombre']} tiene \
{KOMBAT_CONFIG['player2']['health']} energia"""
