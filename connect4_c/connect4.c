#include "connect4_engine.h"
#include <stdio.h>
#include <stdlib.h>
#define EMPTY -1
#define VALID_INPUT 1

/* prototypes */
int print_board(
      int row_size, int column_size, int board[row_size][column_size]);
void initialize(int num_rows, int num_cols, int board[num_rows][num_cols]);

int main(int argc, char* argv[3]) {
    if (argc < 3) {
      printf("Not enough inputs!\n");
      return -1;
    }
    int game_in_session = 1;
    int cell_dimen = atoi(argv[1]);
    int length_to_win = atoi(argv[2]);
    int player;
    int column;
    int board[cell_dimen][cell_dimen];
    printf("Board size: %d x %d, To win: %d\n",
        cell_dimen, cell_dimen, length_to_win);
    initialize(cell_dimen, cell_dimen, board);
    do {
     printf("Ready player: ");
     if (scanf("%d", &player) != VALID_INPUT) {
        printf("Invalid player!\n");
        fpurge(stdin);
        continue;
     }
     printf("Enter column: ");
     if (scanf("%d", &column) != VALID_INPUT) {
         printf("Invalid column!\n");
         fpurge(stdin);
         continue;
     }
     place_token(player, column, cell_dimen, cell_dimen, board);
     int win = winner(cell_dimen, cell_dimen, length_to_win, board);
     if (win >= 0) {
       printf("Win: %d!\n", win);
     }
     print_board(cell_dimen, cell_dimen, board);
    } while(game_in_session);
    return 0;
}

int print_board(int row_size, int column_size,
  int board[row_size][column_size]) {
    for (int i = 0; i < row_size; i++) {
        for (int j = 0; j < column_size; j++) {
            if (board[i][j] == -1) {
              printf("%s  ", ".");
            } else {
              printf("%d  ", board[i][j]);
            }
        }
        printf("\n");
    }
    printf("\n");
    return 0;
}

void initialize(int num_rows, int num_cols, int board[num_rows][num_cols]) {
  int r, c;
  for (r = 0; r < num_rows; r++) {
    for (c = 0; c < num_cols; c++) {
      board[r][c] = EMPTY;
    }
  }
}
