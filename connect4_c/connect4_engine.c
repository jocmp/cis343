#include "connect4_engine.h"

int place_token(int player, int column, int num_rows,
                        int num_columns, int board[num_rows][num_columns]) {
    int column_index = num_columns - 1;
    if (column > column_index || column < 0) {
        // Don't place token if
        return -1;
    }
    return -1;
}

int winner(int num_rows, int num_columns, int length_to_win,
        int array[num_rows][num_columns]) {
    return -1;
}

int check_winner_diagonal_ascend(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    int win_count;
    int player;
    int i;
    int index_size = num_columns - 1;
    for (i = 0; i < index_size; i++) {
      if (array[i][i] == array[i + 1][i + 1]) {
        win_count++;
      } else {
        win_count = 0;
        player = -1;
      }
    }
    if (win_count == length_to_win) {
      return player;
    }
    return -1;
}

int check_winner_diagonal_descend(int num_rows, int num_columns, int length_to_win, int array[num_rows][num_columns]) {
    int win_count;
    int player;
    int i;
    int index_size = num_columns - 1;
    for (i = index_size; i > 0; i--) {
      if (array[i][i] == array[i + 1][i + 1]) {
        win_count++;
      } else {
        win_count = 0;
        player = -1;
      }
    }
    if (win_count == length_to_win) {
      return player;
    }
    return -1;
}
