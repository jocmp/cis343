#include "connect4_engine.h"

int place_token(int player, int column, int num_rows,
                int num_columns, int board[num_rows][num_columns]) {
    int column_index = num_columns - 1;

    if ((column <= column_index) && (column >= 0)) {
        int open_row = open_space(column, num_rows, num_columns, board);
        if (open_row > -1) {
            board[open_row][column] = player;
            return player; // This player was successfully placed
        }
    }
    return -1; // The value should still be empty
}

int winner(int num_rows, int num_columns, int length_to_win,
           int array[num_rows][num_columns]) {
    /* There are four ways to win, but only one way will
     * be greater than -1 each time if there is a win. In this way,
     * we can keep track of the wins with an array of size 4. */
    int wins[4] = {-1};
    int player_one_win = -1;
    int player_two_win = -1;
    int board_full = 0;

    wins[0] = check_winner_vertical(
            num_rows, num_columns, length_to_win, array);
    wins[1] = check_winner_horizontal(
            num_rows, num_columns, length_to_win, array);
    wins[2] = check_winner_diagonal_right_up(
            num_rows, num_columns, length_to_win, array);
    wins[3] = check_winner_diagonal_left_up(
            num_rows, num_columns, length_to_win, array);

    board_full = check_full_board(num_rows, num_columns, array);

    for (int i = 0; i < 4; i++) {
        if (wins[i] == 0)
          player_one_win = 1;
        if (wins[i] == 1)
          player_two_win = 1;
    }

    if (player_one_win == 1) {
        return 0;
    } else if (player_two_win == 1) {
        return 1;
    }

    if (board_full == num_columns) {
        return 2;
    }
    return -1;
}

int check_winner_vertical(int num_rows, int num_columns,
                          int length_to_win, int array[num_rows][num_columns]) {
    int win_count = 0;
    int index_player = -1;

    for (int col = 0; col < num_columns - 1; col++) {
        for (int row = num_rows - 1; row > 0; --row) {
            int current_index = array[row][col];
            if ((win_count == 0) && (current_index != -1)) {
                ++win_count;
            }
            if ((current_index == array[row - 1][col]) && (current_index != -1)) {
                ++win_count;
                index_player = array[row][col];
            } else {
                win_count = 0;
                index_player = -1;
            }
            if (win_count == length_to_win) {
                return index_player;
            }
        }
    }
    return -1;
}

int check_winner_horizontal(int num_rows,
                            int num_columns,
                            int length_to_win,
                            int array[num_rows][num_columns]) {
    int win_count = 0;
    int index_player = -1;

    for (int row = 0; row < num_rows; row++) {
        for (int col = 0; col < num_columns - 1; col++) {
            int current_index = array[row][col];

            if ((win_count == 0) && (current_index != -1)) {
                ++win_count;
            }
            if ((current_index == array[row][col + 1]) && (current_index != -1)) {
                ++win_count;
                index_player = array[row][col];
            } else {
                win_count = 0;
                index_player = -1;
            }
            if (win_count == length_to_win) {
                return index_player;
            }
        }
    }
    return -1;
}

int check_winner_diagonal_right_up(int num_rows,
                                   int num_columns,
                                   int length_to_win,
                                   int board[num_rows][num_columns]) {
    int win_count = -1;
    int extra = 0;
    // The increment for how many "diagonals away from" the left we are
    for (int diag_left = 2; diag_left < num_rows * 2 - 3; diag_left++) {
        extra = 0;
        if (diag_left < num_rows) {
            extra = 0;
        } else {
            extra = diag_left - num_rows + 1;
        }
        win_count = -1;
        for (int index = extra; index <= diag_left - extra; index++) {
            int row = index;
            int col = diag_left - index;

            if ((win_count == 0) && (board[row][col] != -1)) {
                ++win_count;
            }
            if ((board[row - 1][col + 1] == board[row][col])
                && (board[row][col] != -1)) {
                ++win_count;
            } else {
                win_count = 0;
            }

            if (win_count >= length_to_win) {
                return board[row][col];
            }
        }
    }
    return -1;
}

int check_winner_diagonal_left_up(int num_rows,
                                  int num_columns,
                                  int length_to_win,
                                  int board[num_rows][num_columns]) {
    int win_count = -1;
    int extra = 0;
    // The increment for how many "diagonals away from" the left we are
    // We can start with 3 diagonals in, as no board will be under
    // three pieces in length, nor less than three to win.
    for (int diag_right = 2; diag_right < num_rows * 2 - 3; diag_right++) {
        extra = 0;
        if (diag_right < num_rows) {
            extra = 0;
        } else {
            // "Over peak" amount of extra counts
            // Since we keep choosing a new index even though the size
            // of the diagonals is now decreasing
            extra = diag_right - num_rows + 1;
        }
        win_count = -1;
        for (int index = extra; index <= diag_right - extra; index++) {
            int row = index;
            int col = (num_rows - 1) - (diag_right - index);
            if ((win_count == 0) && (board[row][col] != -1)) {
                ++win_count;
            }
            if ((board[row - 1][col - 1] == board[row][col]) &&
                (board[row][col] != -1)) {
                ++win_count;
            } else {
                win_count = 0;
            }
            if (win_count >= length_to_win) {
                return board[row][col];
            }
        }
    }
    return -1;
}

int open_space(int column, int num_rows, int num_columns,
               int board[num_rows][num_columns]) {
    int current_index;

    for (int row = num_rows - 1; row > -1; --row) {
        current_index = board[row][column];

        if (current_index < 0) {
            return row;
        }
    }
    return -1; // No open spaces were found
}

int check_full_board(int num_rows, int num_columns,
                     int board[num_rows][num_columns]) {
    int full_count = 0; // The number of columns that are full
    for (int col = 0; col < num_columns; col++) {
        if (board[0][col] != -1) {
            full_count++;
        }
    }
    return full_count;
}
