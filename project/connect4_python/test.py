import unittest
from Connect4Engine import Connect4Engine


EMPTY = -1

class TestStringMethods(unittest.TestCase):

    ################################################################
    ##
    ## Test winner function
    ##
    ################################################################
    def test_winner_horizontal_r0(self):
        self.engine = Connect4Engine(7, 4, 4)
        self.engine.board.grid[0][0] = 0
        self.engine.board.grid[0][1] = 0
        self.engine.board.grid[0][2] = 0
        self.engine.board.grid[0][3] = 0

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
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
