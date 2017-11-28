
class SudokuBoard(object):
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
                    "Each line in the sudoku puzzle must be 9 chars long."
                )
            board.append([])

            for c in line:
                if not c.isdigit():
                    raise Error(
                        "Valid characters for a sudoku puzzle must be in 0-9"
                    )
                board[-1].append(int(c))

        if len(board) != 9:
            raise Error("Each sudoku puzzle must be 9 lines long")
        return board


class Error(Exception):
    """
    An application specific error.
    """
    pass
