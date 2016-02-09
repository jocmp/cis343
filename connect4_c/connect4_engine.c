#include "connect4_engine.h"
#include <stdio.h>
#include <stdlib.h>


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

int check_winner_diagonal_ascend(int num_rows, int num_columns, int length_to_win,
        int array[num_rows][num_columns]) {
    return -1;
}


int check_winner_diagonal_descend(int num_rows, int num_columns, int length_to_win,
        int array[num_rows][num_columns]) {
    return -1;
}

