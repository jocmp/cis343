#!/usr/bin/env python

from Board import Board


class Connect4Engine:
    def __init__(self, rows, columns, length_to_win):
        self.board = Board(rows, columns)
        self.length_to_win = length_to_win

    def place_token(self, player, column):
        if self.board.columns > column >= 0:
            open_row = self.open_space(column)
            if open_row > -1:
                self.board.grid[open_row][column] = player
                return player  # This player was successfully placed
        return -1  # The value should still be empty

    def winner(self):
        wins = []
        player_one_win = -1
        player_two_win = -1
        wins.append(self.__check_winner_vertical())
        wins.append(self.__check_winner_horizontal())
        wins.append(self.__check_winner_diagonal_up_right())
        wins.append(self.__check_winner_diagonal_left_down())
        board_full = self.__check_full_board()
        for win in wins:
            if win == 0:
                player_one_win = 1
            if win == 1:
                player_two_win = 1
        if player_one_win == 1:
            return 0
        elif player_two_win == 1:
            return 1
        if board_full == self.board.columns:
            return 2
        return -1

    def __check_winner_vertical(self):
        win_count = 0
        for column in xrange(0, self.board.columns - 1):
            for row in xrange(0, self.board.rows - 1):
                current_index = self.board.grid[row][column]
                if win_count == 0 and current_index != -1:
                    win_count += 1
                if current_index == self.board.grid[row - 1][column] and current_index != -1:
                    win_count += 1
                    index_player = self.board.grid[row][column]
                else:
                    win_count = 0
                    index_player = -1
                if win_count == self.length_to_win:
                    return index_player
        return -1

    def __check_winner_horizontal(self):
        win_count = 0
        for row in xrange(0, self.board.rows - 1):
            for column in xrange(0, self.board.columns - 1):
                current_index = self.board.grid[row][column]
                if win_count == 0 and current_index != -1:
                    win_count += 1
                if current_index == self.board.grid[row][column + 1] and current_index != -1:
                    win_count += 1
                    index_player = self.board.grid[row][column]
                else:
                    win_count = 0
                    index_player = -1
                if win_count == self.length_to_win:
                    return index_player
        return -1

    def __check_winner_diagonal_left_down(self):
        rows = self.board.rows
        columns = self.board.columns
        for d_slice in xrange(rows + columns - 1):
            slice_elements = []
            skip_end = 0 if d_slice < columns else d_slice - columns + 1
            skip_start = 0 if d_slice < rows else d_slice - rows + 1
            for j in xrange(d_slice - skip_start, skip_end + 1, -1):
                slice_elements.append(
                    self.board.grid[j][d_slice - j]
                )
            win_count = 0
            for i in xrange(1, len(slice_elements) - 1):
                if win_count == 0 and slice_elements[i] > -1:
                    win_count += 1
                if slice_elements[i + 1] == slice_elements[i] and slice_elements[i] != -1:
                    win_count += 1
                else:
                    win_count = 0
                if win_count >= self.length_to_win:
                    return slice_elements[i]
        return -1

    def __check_winner_diagonal_up_right(self):
        rows = self.board.rows
        columns = self.board.columns
        for d_slice in xrange(rows + columns - 1):
            slice_elements = []
            skip_end = 0 if d_slice < columns else d_slice - columns + 1
            skip_start = 0 if d_slice < rows else d_slice - rows + 1
            for j in xrange(d_slice - skip_start, skip_end + 1, -1):
                slice_elements.append(
                    self.board.grid[rows - j - 1][d_slice - j]
                )
            win_count = 0
            for i in xrange(0, len(slice_elements) - 1):
                if win_count == 0 and slice_elements[i] > -1:
                    win_count += 1
                if slice_elements[i + 1] == slice_elements[i] and slice_elements[i] != -1:
                    win_count += 1
                else:
                    win_count = 0
                if win_count >= self.length_to_win:
                    return slice_elements[i]
        return -1

    def open_space(self, column):
        for row in xrange(self.board.rows - 1, -1, -1):
            current_index = self.board.grid[row][column]
            if current_index < 0:
                return row
        return -1  # No open spaces were found

    def __check_full_board(self):
        full_count = 0  # The number of columns that are full
        for column in xrange(0, self.board.columns):
            if self.board.grid[0][column] != -1:
                full_count += 1
        return full_count
