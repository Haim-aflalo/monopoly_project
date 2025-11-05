import data


class Board:

    def __init__(self):
        self.board = data.tiles_data

    @staticmethod
    def roll_on_board(position):
        if position >= 40:
            position -= 40

    @staticmethod
    def chek_start(position, roll):
        return (position + roll) < position
