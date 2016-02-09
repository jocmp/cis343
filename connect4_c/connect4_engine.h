#ifndef H_CONNECT4_ENGINE
#define H_CONNECT4_ENGINE

int current_board_size;

int place_token(int player, int column, int num_rows, 
        int num_columns, int board[num_rows][num_columns]);

int winner(int num_rows, int num_columns, int length_to_win,
        int array[num_rows][num_columns]);


int check_winner_diagonal_ascend(int num_rows, int num_columns, int length_to_win,
        int array[num_rows][num_columns]);

int check_winner_diagonal_descend(int num_rows, int num_columns, int length_to_win,
        int array[num_rows][num_columns]);
#endif
