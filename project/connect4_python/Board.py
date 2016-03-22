#!/usr/bin/env python

class Board:
    """docstring for Board"""

    def __init__(self, dimension):
        self.rows = dimension
        self.columns = dimension
        self.grid = [[-1 for x in xrange(self.rows)] for y in xrange(self.columns)]

    def __str__(self):
        print_board = ""
        for i in xrange(0, self.rows):
            for j in xrange(0, self.columns):
                if self.grid[i][j] == -1:
                    print_board += ".  "
                else:
                    print_board += str(self.grid[i][j]) + "  "
            print_board += "\n"

        return print_board
