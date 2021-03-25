# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:
# -----------------------------------------------------------------------------
'''
Enter the module docstring here
'''
import tkinter
import math
from random import random, randrange, seed

class Game(object):
    '''
    Creates a game of tic tac toe
    '''

    # Add your class variables if needed here - square size, etc...)
    square_size = 150
    colors = ['WHITE', 'RED', 'BLUE']

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        # Create the restart button widget
        # Create a canvas widget
        # Create a label widget for the win/lose message
        # Create any additional instance variable you need for the game
        self.parent = parent
        self.initialize_game()

    def initialize_game(self):
        '''
        This method initializes the game with a blank board and creates all the
        label elements
        :return:
        '''
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.top_of_board = tkinter.Frame(self.parent)
        self.top_of_board.pack(side=tkinter.TOP)

        # add restart button on top frame
        restart_button = tkinter.Button(self.top_of_board, text='Restart',
                                        width=20,
                                        command=self.restart)
        restart_button.pack()  # register restart_button

        # create bottom frame for group the label below
        self.bottom_of_board = tkinter.Frame(self.parent)
        self.bottom_of_board.pack(side=tkinter.BOTTOM)

        # create label for displaying game result text
        self.my_lbl = tkinter.Label(self.bottom_of_board, text=None)
        self.my_lbl.pack()

        # create a canvas to draw our board on the top frame
        self.canvas = tkinter.Canvas(self.top_of_board,
                                     width=self.square_size * 3,
                                     height=self.square_size * 3)
        self.board_locked = False
        self.draw_board()


    def draw_board(self):
        '''
        This method generates a blank board filled with 9 white rectangles
        :return:
        '''
        for row in range(3):
            for column in range(3):
                self.canvas.create_rectangle(self.square_size * column,
                                             self.square_size * row,
                                             self.square_size * (column + 1),
                                             self.square_size * (row + 1),
                                             fill='white')
            self.canvas.bind("<Button-1>", self.play)
            self.canvas.pack()

    def restart(self):
        '''
        This method destroys all elements on the canvas
        and then reinitializes them
        :return:
        '''
        self.top_of_board.destroy()
        self.bottom_of_board.destroy()
        self.initialize_game()

    def play(self, event):
        x = int(self.clamp(event.x) / Game.square_size)
        y = int(self.clamp(event.y) / Game.square_size)

        if self.board[x][y] is 0 and not self.board_locked:
            self.board[x][y] = 1

            shape = self.canvas.find_closest(event.x, event.y)
            self.canvas.itemconfigure(shape, fill=Game.colors[1])

            if self.get_winner(1):
                self.display_winner(1)
                self.board_locked = True
            elif self.check_tie():
                self.display_winner(0)
                self.board_locked = True
            else:
                #pick a random free tile
                tile = self.pick_rand_tile()
                x = tile[0]
                y = tile[1]
                if self.board[x][y] is 0 and not self.board_locked:
                    self.board[x][y] = 2

                    shape = self.canvas.find_closest(x * Game.square_size,
                                                     y * Game.square_size)
                    self.canvas.itemconfigure(shape, fill=Game.colors[2])

                    if self.get_winner(2):
                        self.display_winner(2)
                        self.board_locked = True
                    elif self.check_tie():
                        self.display_winner(0)
                        self.board_locked = True

    def get_winner(self, player):
        '''
        This method checks for a winner in
        each of the directions- vertical horizontal and both diagonal
        :param player: which player int to check for
        :return: True / False
        '''
        for x in range(len(self.board)):
            if self.board[x][0] == self.board[x][1] == \
               self.board[x][2] == player:
                return True
        for y in range(len(self.board)):
            if self.board[0][y] == self.board[1][y] == \
               self.board[2][y] == player:
                return True
        if self.board[0][0] == self.board[1][1] == \
           self.board[2][2] == player:
            return True
        if self.board[2][0] == self.board[1][1] == \
           self.board[0][2] == player:
            return True

    def check_tie(self):
        '''
        This method checks for all tiles on the board being played upon (tile)
        :return: True / False
        '''
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] is 0:
                    return False
        return True

    def display_winner(self, winner):
        '''
        This method modifies the text label containing
        the win text to match whatever side won (or none).
        :param winner:
        :return:
        '''
        if winner is 1:
            self.my_lbl.config(text='RED WINS!')
        elif winner is 2:
            self.my_lbl.config(text='BLUE WINS!')
        else:
            self.my_lbl.config(text='TIE!')

    def pick_rand_tile(self):
        '''
        This returns a random open tile in the board
        :return: tuple containing the 2d matrix coords
        '''

        x = randrange(0, len(self.board))
        y = randrange(0, len(self.board))
        while (self.board[x][y] is not 0):
            x = randrange(0, len(self.board))
            y = randrange(0, len(self.board))
        return (x,y)

    def clamp(self, val):
        '''
        This helper method clamps the x and y canvas coords
        to be inside the min / max bounds of the board
        :param val:
        :return:
        '''
        return max(min(val, Game.square_size*3), 0)


def main():
    # Instantiate a root window
    # Instantiate a Game object
    # Enter the main event loop

    root = tkinter.Tk()  # Instantiate a root window
    the_game = Game(root)  # Instantiate a Game object
    root.mainloop()  # Enter the main event loop

if __name__ == '__main__':
    main()