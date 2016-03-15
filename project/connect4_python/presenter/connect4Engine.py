from model import Board
from model import Player

class Connect4Engine(object):
    """ Driver file for Connect 4 program
    """
    def __init__(self, dimension):
        super(Connect4Engine, self).__init__()
        self.board = Board(dimension)
        print self.board

    def place_token(self, player, column):
        column_index = self.board.columns - 1
        if column < column_index and column >= 0:
            open_row = self.open_space(column)
            if open_row > -1:
                self.board.grid[open_row][column] = player.id
                return player.id # This player was successfully placed
        return -1 # The value should still be empty

    def open_space(self, column):
        current_index = 0
        for row in xrange(self.board.rows, -1, -1):
            current_index = self.board[row][column]
            if current_index < 0:
                return row
        return -1 # No open spaces were found

    def check_full_board(self):
        full_count = 0 # The number of columns that are full
        for column in xrange(0, self.board.columns):
            if self.board.grid[0][column] != -1:
                full_count += 1
        return full_count

    # def check_winner_vertical(self):