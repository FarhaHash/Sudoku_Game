import Sudoku
import GUI

from tkinter import *
import os
import random
EASY= ['Easy1.sudoku','Easy2.sudoku','Easy3.sudoku']
MEDIUM=['Medium1.sudoku','Medium2.sudoku','Medium3.sudoku']
HARD=['Hard1.sudoku','Hard2.sudoku','Hard3.sudoku']
VERYHARD=['VeryHard1.sudoku','VeryHard2.sudoku','VeryHard3.sudoku']
INVALID_TEXT = """Select a valid level!"""
ABOUT_TEXT = """                                                            
Sudoku is the Japanese abbreviation of a phrase meaning the digits must remain single, also known as Number Place, where Su means number, doku which translates as single or bachelor.  It is a logic based number placement puzzle.  The aim of this puzzle is to fill a 9X9 gird so that each column, each row, and each of the nine 3X3 boxes (blocks/regions) contains the digits from 1 through 9 , without repetition.  In this game, a player is given a grid in which some of the cells are filled in from the beginning and must complete filling in the grid by entering the remaining numbers.  The rules are simple, but some puzzles can get very difficult, and it attracts fans from all over the world.   

The objective of sudoku is to enter a digit from 1 through 9 in each cell, in such a way that:

1.Each horizontal row contains each digit exactly once.
2.Each vertical column contains each digit exactly once.
3.Each sub grid or region contains each digit exactly once.
"""


class StartGame(object):

    def __init__(self, root):
        self.root = root
        self.root.geometry("500x660")
        self.__draw_menu()
        self.__draw_label()


    def game(self, boards_file,name):
        frame = Frame(self.root)
        frame.pack(fill=BOTH, side=TOP)
        Label(frame, text="Here is the puzzle "+name+". Good luck!" , foreground="brown",bd=20, font='-weight bold').pack()
        game = Sudoku.Game(boards_file)
        game.start()
        GUI.GUI(self.root, game)
        self.root.geometry("500x660")


    def __draw_label(self):
        self.frame1 = Frame(self.root)
        self.frame1.pack(fill=BOTH, side=TOP)
        self.frame2 = Frame(self.root)
        self.frame2.pack(fill=BOTH, side=TOP)
        self.frame3 = Frame(self.root)
        self.frame3.pack(fill=BOTH, side=TOP)
        Label(self.frame1, text="Player Name                                                         ").pack(side=LEFT)
        self.e1 = Entry(self.frame1)
        self.e1.pack()
        Label(self.frame2, text="Select a puzzle...(Easy, Medium, Hard or Evil!)").pack(side=LEFT)
        self.e2 = Entry(self.frame2)
        self.e2.pack()
        self.submit_button = Button(self.frame3,
                                    text="SUBMIT", fg="blue", width=25,
                                    command=self.__submit)

        self.submit_button.pack()

    def __submit(self):
        if self.e2.get().lower() == "Easy".lower():
            self.easy_level()
        elif self.e2.get().lower() == "Medium".lower():
            self.medium_level()
        elif self.e2.get().lower() == "Hard".lower():
            self.hard_level()
        elif self.e2.get().lower() == "Evil".lower():
            self.veryhard_level()
        elif self.e2.get().lower() == "debug".lower():
            self.debug_game()
        else:
            toplevel = Toplevel()
            label1 = Label(toplevel, text=INVALID_TEXT, height=5, width=50)
            label1.pack()


    def __draw_menu(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.file = Menu(self.menu, tearoff=0)
        self.about = Menu(self.menu, tearoff=0)
        self.file.add_command(label="Restart", command=self.restart_game)
        self.file.add_command(label="Close", command=self.exit_game)
        self.about.add_command(label="Info", command=self.about_game)
        self.menu.add_cascade(label="File", menu=self.file)
        self.menu.add_cascade(label="About", menu=self.about)

    def about_game(self):
        toplevel = Toplevel()
        text = Text(toplevel)
        text.insert(INSERT, ABOUT_TEXT)
        text.pack()

    def easy_level(self):
        filename=random.choice(EASY)
        boards_file = open(filename, 'r')
        self.game(boards_file, self.e1.get())

    def medium_level(self):
        filename=random.choice(MEDIUM)
        boards_file = open(filename, 'r')
        self.game(boards_file,self.e1.get())

    def hard_level(self):
        filename=random.choice(HARD)
        boards_file = open(filename, 'r')
        self.game(boards_file,self.e1.get())

    def veryhard_level(self):
        filename=random.choice(VERYHARD)
        boards_file = open(filename, 'r')
        self.game(boards_file,self.e1.get())

    def debug_game(self):
        boards_file = open('debug.sudoku', 'r')
        self.game(boards_file,self.e1.get())

    def exit_game(self):
        exit()

    def restart_game(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)
