#include "connect4_engine.h"

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
    return -1;
}

int check_winner_vertical(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    return -1;
}

int check_winner_horizontal(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    return -1;
}

int check_winner_diagonal_ascend(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    int i = num_rows - 1; // row index
    int j = 0; // column index
    int top = 1;
    int cols_index_max = num_columns - 2;
    int win_count = 0;
    int current_winning_player = -1;
    for (; i < top; i--) {
      for (j = 0; j < cols_index_max; j++) {
        if (arr[i][j] == arr[i + 1][j + 1]) {
          win_count++;
          current_winning_player = arr[i][j];
        } else {
          win_count = 0;
          current_winning_player = -1;
        }
      }
    }
    if (win_count >= length_to_win) {
      return current_winning_player;
    }
    return -1;
}

int check_winner_diagonal_descend(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    int i = 0; // row index
    int j = 0; // column index
    int row_index_max = num_rows - 2;
    int cols_index_max = num_columns - 2;
    int win_count = 0;
    int current_winning_player = -1;
    for (i = 0; i < row_index_max; i++) {
      for (j = 0; j < cols_index_max; j++) {
        if (arr[i][j] == arr[i + 1][j + 1]) {
          win_count++;
          current_winning_player = arr[i][j];
        } else {
          win_count = 0;
          current_winning_player = -1;
        }
      }
    }
    if (win_count >= length_to_win) {
      return current_winning_player;
    }
    return -1;
}
