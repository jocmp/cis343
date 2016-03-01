#ifndef H_CONNECT4_ENGINE
#define H_CONNECT4_ENGINE

int place_token(int player, int column, int num_rows,
                int num_columns, int board[num_rows][num_columns]);

int winner(int num_rows, int num_columns, int length_to_win,
           int array[num_rows][num_columns]);

int print_board(
        int row_size, int column_size, int board[row_size][column_size]);

void initialize(int num_rows, int num_cols, int board[num_rows][num_cols]);

void check_valid_input(int *input);

void print_winner(int winner);

/* Non-"global" prototypes */
int check_winner_vertical(int num_rows,
                          int num_columns,
                          int length_to_win,
                          int array[num_rows][num_columns]);

int check_winner_horizontal(int num_rows,
                            int num_columns,
                            int length_to_win,
                            int array[num_rows][num_columns]);

int check_winner_diagonal_left_up(int num_rows, int num_columns,
                                  int length_to_win,
                                  int array[num_rows][num_columns]);

int check_winner_diagonal_right_up(int num_rows, int num_columns,
                                   int length_to_win,
                                   int array[num_rows][num_columns]);

int open_space(int column, int num_rows,
               int num_columns,
               int array[num_rows][num_columns]);

int check_full_board(int num_rows, int num_columns,
                     int array[num_rows][num_columns]);

#endif
