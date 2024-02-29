# tic_tac_toe\logic\exceptions.py

class InvalidGameState(Exception):
    """Raised whnever the game state is invalid"""


class InvalidMove(Exception):
    """Raised whenever the move is invlaid"""
