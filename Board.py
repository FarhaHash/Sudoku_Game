
class Board(object):
    """
    Sudoku Board representation
    """

    def __init__(self, board_file):
        self.board = self.__create_board(board_file)

    def __create_board(self, board_file):
        board = []
        for line in board_file:
            line = line.strip()
            if len(line) != 9:
                raise Error(
                    "Each row must contain 9 numbers!"
                )
            board.append([])

            for c in line:
                if not c.isdigit():
                    raise Error(
                        "Only 0-9 numbers are valid for Sudoku puzzle!"
                    )
                board[-1].append(int(c))

        if len(board) != 9:
            raise Error("Each row must contain 9 numbers!")
        return board


class Error(Exception):
    """
    An application specific error.
    """
    pass
