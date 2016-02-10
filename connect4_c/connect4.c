#include "connect4_engine.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[3]) {
    if (argc < 3) {
      printf("Not enough inputs!\n");
      return -1;
    }
    int cell_dimen = atoi(argv[1]);
    int num_to_win = atoi(argv[2]);
    printf("Board size: %d x %d, To win: %d\n",
        cell_dimen, cell_dimen, num_to_win);
    return 0;
}
