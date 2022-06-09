"""Business logic, or fight choreography"""
MAX_HEALTH = 6
MAX_MOVEMENTS = 5
MAX_STRIKES = 1
ALLOWED_MOVEMENTS = "WSAD"
ALLOWED_STRIKES = "PK"

TONYN_COMBINATIONS = {
    "Taladoken": {"MOVEMENTS": "DSD", "STRIKE": "P", "DAMAGE": 3},
    "Remuyuken": {"MOVEMENTS": "SD", "STRIKE": "K", "DAMAGE": 2},
    "Strike": {"MOVEMENTS": "", "STRIKE": "PK", "DAMAGE": 1},
}

ARNALDOR_COMBINATIONS = {
    "Remuyuken": {"MOVEMENTS": "SA", "STRIKE": "K", "DAMAGE": 3},
    "Taladoken": {"MOVEMENTS": "ASA", "STRIKE": "P", "DAMAGE": 2},
    "Strike": {"MOVEMENTS": "", "STRIKE": "PK", "DAMAGE": 1},
}


def get_relato(kombat: dict) -> list:
    narration = []
    first_player = define_first(kombat)
    narration.append(
        f"First player is {first_player}, movements are {kombat[first_player]}"
    )
    return narration


def define_first(kombat: dict) -> str:
    mov_tony = len(kombat["player1"]["movimientos"])
    gol_tony = len(kombat["player1"]["golpes"])
    mov_arnal = len(kombat["player2"]["movimientos"])
    gol_arnal = len(kombat["player2"]["golpes"])
    comb_tony = mov_tony + gol_tony
    comb_arnal = mov_arnal + gol_arnal

    if comb_tony != comb_arnal:
        return "player1" if comb_tony > comb_arnal else "player2"

    if mov_tony != mov_arnal:
        return "player1" if mov_tony > mov_arnal else "player2"

    if gol_tony != gol_arnal:
        return "player1" if gol_tony > gol_arnal else "player2"

    return "player1"


def generate_fight_report():
    return