#include "connect4_engine.h"

/* arrays are pointers! if they're passed, they modify
 * the overall reference */

int place_token(int player, int column, int num_rows,
                        int num_columns, int board[num_rows][num_columns]) {
    int column_index = num_columns - 1;
    if (column > column_index || column < 0) {
        // Don't place token if
        return ;
    }
    return -1;
}

int winner(int num_rows, int num_columns, int length_to_win,
        int array[num_rows][num_columns]) {
          int wins[4] = -1;
          int player_one_win = -1;
          int player_two_win = -1;
          wins[0] = check_winner_vertical(num_rows, num_columns, length_to_win, array);
          wins[1] = check_winner_horizontal(num_rows, num_columns, length_to_win, array);
          wins[2] = check_winner_diagonal_right_down(
                      num_rows, num_columns, length_to_win, array);
          wins[3] = check_winner_diagonal_left_down(
                      num_rows, num_columns, length_to_win, array);
          for(int i = 0; i < 3; i++) {
            switch (win[i]) {
              case 0:
                player_one_win = 1;
                break;
              case 1:
                player_two_win = 1;
                break;
              default:
                break;
            }
          }
          if (player_one_win && player_two_win) {
            return 2;
          } else if (player_one_win) {
            return 0;
          } else if (player_two_win) {
            return 1
          }
          return -1;
}

int check_winner_vertical(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    int max_col_index = num_columns - 2;
    int max_row_index = num_rows - 2;
    int win_count = 0;
    int index_player = -1;

    for (int col = 0; col < max_col_index; col++) {
        for (int row = 0; row < max_row_index; row++) {
           int current_index = array[row][col];
           if (current_index == array[row + 1][col] && current_index != -1) {
               win_count++;
               index_player = array[row][col];
               if (win_count == length_to_win) {
                   return index_player;
               }
           } else {
                win_count = 0;
                index_player = -1;
           }
        }
    }
    return -1;
}

int check_winner_horizontal(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    int max_col_index = num_columns - 2;
    int max_row_index = num_rows - 2;
    int win_count = 0;
    int index_player = -1;

    for (int row = 0; row < max_row_index; row++) {
        for (int col = 0; col < max_col_index; col++) {
           int current_index = array[row][col];
           if (current_index == array[row + 1][col] && current_index != -1) {
               win_count++;
               index_player = array[row][col];
               if (win_count == length_to_win) {
                   return index_player;
               }
           } else {
                win_count = 0;
                index_player = -1;
           }
        }
    }
    return -1;
}

int check_winner_diagonal_right_down(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    for (int diag_right = 2; diag_right < diag_max * 2 - 3; diag_right++) {
        int extra;
        if (diag_right < diag_max) {
          extra = 0;
        } else {
          // "Over peak" amount of extra counts
          // Since we keep choosing a new index even though the size
          // of the diagonals is now decreasing
          extra = diag_right - diag_max + 1;
        }
        win_count = -1;
        for (int index = extra; index <= diag_right - extra; index++) {
            int row = index;
            int col = (diag_max - 1) - (diag_right - index);
            if (win_count == 0 && board[row][col] != -1) {
                ++win_count;
            }
            printf("%d ", board[row][col]);
            if (board[row - 1][col - 1] == board[row][col] &&
                  board[row][col] != -1) {
              ++win_count;
            } else {
              win_count = 0;
            }
            if (win_count >= lenght_to_win) {
                printf("\tWe have a winner of %d!", win_count);
            }
        }
    return -1;
}

int check_winner_diagonal_left_down(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    for (int diag_left = 2; diag_left < num_rows * 2 - 3; diag_left++) {
        int extra;
        if (diag_left < diag_max) {
          extra = 0;
        } else {
          extra = diag_left - diag_max + 1;
        }
        win_count = -1;
        for (int index = extra; index <= diag_left - extra; index++) {
            int row = index;
            int col = diag_left - index;
            if (win_count == 0 && board[row][col] != -1) {
                ++win_count;
            }
            if (board[row - 1][col + 1] == board[row][col]
                      && board[row][col] != -1) {
              ++win_count;
            } else {
              win_count = 0;
            }
            if (win_count >= lenght_to_win) {
              return board[row][col];
            }
        }
    }
    return -1;
}
