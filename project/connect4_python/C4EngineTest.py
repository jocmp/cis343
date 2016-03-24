import unittest
from modules.Connect4Engine import Connect4Engine

EMPTY = -1
NO_WINNER_YET = -1

class C4EngineTest(unittest.TestCase):

    ################################################################
    ##
    ## Test winner function
    ##
    ################################################################

    def test_winner_horizontal_r0(self):
        self.engine = Connect4Engine(7, 4, 4)
        for i in xrange(4):
            self.engine.board.grid[0][i] = 0
        answer = self.engine.winner()
        self.assertEqual(answer, 0, "0s in bottom row")

    def test_winner_diagonal_down_r48(self):
        self.engine = Connect4Engine(100, 100, 7)
        for i in xrange(48, 55):
            self.engine.board.grid[i][i + 2] = 0

        answer = self.engine.winner()
        self.assertEqual(answer, 0, "Centered diagonal win")

    def test_winner_diagonal_up_r48(self):
        self.engine = Connect4Engine(100, 100, 7)
        row_counter = 48
        column_counter = 48
        while row_counter > 41:
            self.engine.board.grid[row_counter][column_counter] = 0
            row_counter -= 1
            column_counter += 1

        answer = self.engine.winner()
        self.assertEqual(answer, 0, "Centered diagonal win")

    def test_loser_diagonal_r48(self):
        self.engine = Connect4Engine(100, 100, 7)
        for i in xrange(48, 55):
            self.engine.board.grid[i][i + 2] = 0

        # Win skip
        self.engine.board.grid[49][51] = 1
        answer = self.engine.winner()
        self.assertEqual(answer, -1, "Centered diagonal loss")

    ################################################################
    ##
    ## Test place_token function
    ##
    ################################################################

    def test_place_token_c1(self):
        rows = 7
        columns = 7
        self.engine = Connect4Engine(rows, columns, 4)
        # make sure there is a 1 at the bottom of column 3
        # and a -1 everywhere else
        self.engine.place_token(1, 3)
        self.assertEqual(self.engine.board.grid[rows - 1][3], 1, "Drop 1 into empty column 3")
        for row in xrange(rows):
            for column in xrange(columns):
                if row != (rows - 1) or column != 3:
                    self.assertEqual(
                        self.engine.board.grid[row][column], EMPTY, "Should be empty")

    def test_place_token_c5(self):
        rows = 7
        columns = 7
        self.engine = Connect4Engine(rows, columns, 4)
        self.engine.place_token(1, 5)
        self.assertEqual(self.engine.board.grid[rows - 1][5], 1, "Drop 1 into empty column 5")
        self.engine.place_token(1, 5)
        self.assertEqual(self.engine.board.grid[rows - 2][5], 1, "Drop 1 into column 5 on 1 full")
        self.engine.place_token(1, 5)
        self.assertEqual(self.engine.board.grid[rows - 3][5], 1, "Drop 1 into column 5 on 2 full")
        for row in xrange(rows):
            for column in xrange(columns):
                if row < (rows - 3) or column != 5:
                    self.assertEqual(
                        self.engine.board.grid[row][column], EMPTY, "Should be empty")

    def test_place_token_c99(self):
        rows = 100
        columns = 100
        self.engine = Connect4Engine(rows, columns, 4)
        self.engine.place_token(1, 99)
        self.assertEqual(self.engine.board.grid[rows - 1][99], 1, "Drop 1 into empty column 99")
        for row in xrange(rows):
            for column in xrange(columns):
                if row != rows - 1 or column != 99:
                    self.assertEqual(self.engine.board.grid[row][column], EMPTY, "Should be empty")

    ################################################################
    ##
    ## Test place_token function
    ##
    ################################################################

    def test_check_full_board_pass(self):
        rows = 4
        columns = 5
        self.engine = Connect4Engine(rows, columns, 4)
        for row in xrange(rows - 1, -1, -1):
            for column in xrange(columns):
                # A number which is not -1
                self.engine.board.grid[row][column] = 0
        answer = self.engine.board_full()
        self.assertEqual(answer, True, "Board should be full")

    def test_check_full_board_fail(self):
        rows = 6
        columns = 9
        self.engine = Connect4Engine(rows, columns, 4)
        # Fill all but the "top" row
        for row in xrange(rows - 1, 0, -1):
            for column in xrange(columns):
                # A number which is not -1
                self.engine.board.grid[row][column] = 0
        # Fill one cell in "top" row
        self.engine.board.grid[0][3] = 1
        answer = self.engine.board_full()
        self.assertEqual(answer, False, "Only one cell should be filled in top row")

    ################################################################
    ##
    ## Test place_token function
    ##
    ################################################################

    def test_horizontal_row0(self):
        rows = 7
        columns = 9
        self.engine = Connect4Engine(rows, columns, 4)
        self.engine.place_token(0, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Single 0 in column 0")
        self.engine.place_token(0, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "0s in columns [0, 1]")
        self.engine.place_token(0, 2)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "0s in columns [0, 1, 2]")
        self.engine.place_token(0, 3)
        self.assertEqual(self.engine.winner(), 0, "4 in a row, horizontal")

    def test_vertical_column1(self):
        rows = 8
        columns = 10
        self.engine = Connect4Engine(rows, columns, 4)
        self.engine.place_token(0, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Single 0 in column 1")
        self.engine.place_token(0, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Two 0s in column 1")
        self.engine.place_token(0, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Three 0s in column 1")
        self.engine.place_token(0, 1)
        self.assertEqual(self.engine.winner(), 0, "4 in a row, vertical")

    def test_diagonal_right_up_3(self):
        rows = 4
        columns = 3
        self.engine = Connect4Engine(rows, columns, 3)
        self.engine.place_token(0, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 1")
        self.engine.place_token(1, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 2")
        self.engine.place_token(0, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 3")
        self.engine.place_token(1, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 4")
        self.engine.place_token(0, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 4")
        self.engine.place_token(1, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 5")
        self.engine.place_token(0, 2)
        self.assertEqual(self.engine.winner(), 0, "Step 6 -- Winner!")

    def test_diagonal_left_down_3(self):
        rows = 4
        columns = 3
        self.engine = Connect4Engine(rows, columns, 3)
        self.engine.place_token(0, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 1")
        self.engine.place_token(1, 2)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 2")
        self.engine.place_token(0, 2)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 3")
        self.engine.place_token(1, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 4")
        self.engine.place_token(0, 2)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 5")
        self.engine.place_token(1, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 6")
        self.engine.place_token(0, 1)
        self.assertEqual(self.engine.winner(), 0, "Step 7 -- Winner!")

    def test_cats_game_4(self):
        '''
        End game:
        1 0 1 1
        0 1 0 0
        1 0 0 0
        0 1 0 1
        '''
        rows = 4
        columns = 4
        self.engine = Connect4Engine(rows, columns, 4)

        # Column 0
        self.engine.place_token(0, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 1")
        self.engine.place_token(1, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 2")
        self.engine.place_token(0, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 3")
        self.engine.place_token(1, 0)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 4")

        # Column 1
        self.engine.place_token(1, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 5")
        self.engine.place_token(0, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 6")
        self.engine.place_token(1, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 7")
        self.engine.place_token(0, 1)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 8")

        # Column 2
        self.engine.place_token(0, 2)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 9")
        self.engine.place_token(0, 2)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 10")
        self.engine.place_token(0, 2)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 11")
        self.engine.place_token(1, 2)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 12")

        # Column 3
        self.engine.place_token(1, 3)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 13")
        self.engine.place_token(0, 3)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 14")
        self.engine.place_token(0, 3)
        self.assertEqual(self.engine.winner(), NO_WINNER_YET, "Step 15")
        self.engine.place_token(1, 3)
        self.assertEqual(self.engine.winner(), 2, "Step 16 -- Winner!")

if __name__ == '__main__':
    unittest.main()
