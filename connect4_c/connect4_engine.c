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
    check_winner_vertical(num_rows, num_columns, length_to_win, array);
    check_winner_horizontal(num_rows, num_columns, length_to_win, array);
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

int check_winner_diagonal_ascend(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    return -1;
}

int check_winner_diagonal_descend(int num_rows, int num_columns,
  int length_to_win, int array[num_rows][num_columns]) {
    return -1;
}
