#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[2]) {
    // int board[3][3] = {{1, -1, 1}, {-1, 1, -1}, {1, -1, 1}};
    int board[4][4] = {{-1, -1, -1, -1}, {-1, -1, -1, 1}, {-1, -1, 1, 1}, {0, 1, 0, 1}};
    int diag_max = 4;
    int win_count = 0;
    int lenght_to_win = 3;
    // The increment for how many "diagonals away from" the right we are

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
        printf("\n");
    }

    printf("\n");
    // The increment for how many "diagonals away from" the left we are
    for (int diag_left = 2; diag_left < diag_max * 2 - 3; diag_left++) {
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
            printf("%d ", board[row][col]);
            if (board[row - 1][col + 1] == board[row][col] && board[row][col] != -1) {
              ++win_count;
            } else {
              win_count = 0;
            }
            if (win_count >= lenght_to_win) {
                printf("\tWe have a winner of %d!", win_count);
            }
        }
        printf("\n");
    }
    return 0;
}
