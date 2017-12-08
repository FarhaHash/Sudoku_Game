from tkinter import *

BOARD_MARGIN = 20
BOARD_SIDE = 50  # Width of every board cell.
BOARD_WIDTH = BOARD_HEIGHT = BOARD_MARGIN * 2 + BOARD_SIDE * 9

class GUI(Frame):
    """
        The Tkinter UI, responsible for drawing the board and accepting user input.
        """

    def __init__(self, parent, game):

        self.game = game
        Frame.__init__(self, parent)
        self.parent = parent
        self.puzzle_row, self.puzzle_col = -1, -1
        self.__initUI()

    def __initUI(self):

        self.parent.title("Sudoku")
        self.pack(fill=BOTH)

        self.canvas = Canvas(self,
                             width=BOARD_WIDTH,
                             height=BOARD_HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)

        clear_button = Button(self,
                              text="RESET", fg="blue", width=25,
                              command=self.__clear_answers)
        clear_button.pack(side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = BOARD_MARGIN + i * BOARD_SIDE
            y0 = BOARD_MARGIN
            x1 = BOARD_MARGIN + i * BOARD_SIDE
            y1 = BOARD_HEIGHT - BOARD_MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = BOARD_MARGIN
            y0 = BOARD_MARGIN + i * BOARD_SIDE
            x1 = BOARD_WIDTH - BOARD_MARGIN
            y1 = BOARD_MARGIN + i * BOARD_SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self):

        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.puzzle[i][j]
                if answer != 0:
                    x = BOARD_MARGIN + j * BOARD_SIDE + BOARD_SIDE / 2
                    y = BOARD_MARGIN + i * BOARD_SIDE + BOARD_SIDE / 2
                    original = self.game.start_puzzle[i][j]
                    color = "black" if answer == original else "blue"
                    self.canvas.create_text(
                        x, y, text=answer, tags="numbers", fill=color
                    )

    def __draw_cursor(self):

        self.canvas.delete("cursor")
        if self.puzzle_row >= 0 and self.puzzle_col >= 0:
            x0 = BOARD_MARGIN + self.puzzle_col * BOARD_SIDE + 1
            y0 = BOARD_MARGIN + self.puzzle_row * BOARD_SIDE + 1
            x1 = BOARD_MARGIN + (self.puzzle_col + 1) * BOARD_SIDE - 1
            y1 = BOARD_MARGIN + (self.puzzle_row + 1) * BOARD_SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor")

    def __draw_victory(self):
        # create a oval (which will be a circle)

        x0 = y0 = BOARD_MARGIN + BOARD_SIDE * 2
        x1 = y1 = BOARD_MARGIN + BOARD_SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="victory", fill="green", outline="black"
        )
        # create text
        x = y = BOARD_MARGIN + 4 * BOARD_SIDE + BOARD_SIDE / 2
        self.canvas.create_text(
            x, y,
            text="You win!", tags="victory",
            fill="white", font=("Arial", 32))

    def __cell_clicked(self, event):

        if self.game.game_over:
            return
        x, y = event.x, event.y
        if (BOARD_MARGIN < x < BOARD_WIDTH - BOARD_MARGIN and BOARD_MARGIN < y < BOARD_HEIGHT - BOARD_MARGIN):
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            puzzle_row, puzzle_col = (y - BOARD_MARGIN) / BOARD_SIDE, (x - BOARD_MARGIN) / BOARD_SIDE

            self.puzzle_row, self.puzzle_col = int(puzzle_row), int(puzzle_col)
        else:
            self.puzzle_row, self.puzzle_col = -1, -1

        self.__draw_cursor()

    def __key_pressed(self, event):

        if self.game.game_over:
            return

        if self.puzzle_row >= 0 and self.puzzle_col >= 0 and event.char in "1234567890":
                self.game.puzzle[self.puzzle_row][self.puzzle_col] = int(event.char)
                self.puzzle_col, self.puzzle_row = -1, -1
                self.__draw_puzzle()
                self.__draw_cursor()
                if self.game.check_win():
                    self.__draw_victory()
        elif event.char not in "1234567890":
            toplevel = Toplevel()
            label1 = Label(toplevel, text="Enter only Numbers[0-9]", height=5, width=50)
            label1.pack()

    def __clear_answers(self):
        self.game.start()
        self.canvas.delete("victory")
        self.__draw_puzzle()
