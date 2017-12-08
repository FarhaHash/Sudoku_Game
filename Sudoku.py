import Board


class Game(object):

    def __init__(self, board_file):
        self.board_file = board_file
        self.start_puzzle = Board.Board(board_file).board

    def start(self):
        self.game_over = False
        self.puzzle = []
        for i in range(9):
            self.puzzle.append([])
            for j in range(9):
                self.puzzle[i].append(self.start_puzzle[i][j])

    def check_win(self):

        # Check for victory

        for puzzle_row in range(9):
            if not self.__check_row(puzzle_row):
                return False
        for puzzle_column in range(9):
            if not self.__check_column(puzzle_column):
                return False
        for puzzle_row in range(3):
            for puzzle_column in range(3):
                if not self.__check_square(puzzle_row, puzzle_column):
                    return False
        self.game_over = True
        return True

    def __check_block(self, block):
        return set(block) == set(range(1, 10))

    def __check_row(self, puzzle_row):
        return self.__check_block(self.puzzle[puzzle_row])

    def __check_column(self, puzzle_column):
        return self.__check_block(
            [self.puzzle[puzzle_row][puzzle_column] for puzzle_row in range(9)])

    def __check_square(self, puzzle_row, puzzle_column):
        return self.__check_block([
                self.puzzle[r][c]
                for r in range(puzzle_row * 3, (puzzle_row + 1) * 3)
                for c in range(puzzle_column * 3, (puzzle_column + 1) * 3)])