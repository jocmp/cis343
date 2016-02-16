#include <stdio.h>
#include <stdlib.h>

void nested_descend(int dimen, int win) {
    int dimen_array[dimen][dimen];
    int i;
    int j;
    for (i = 0; i < dimen; i++) {
        for (j = 0; j < dimen; j++) {
            dimen_array[i][j] = dimen * i + j;
            printf("%d\t", dimen_array[i][j]);
        }
        printf("\n");
    }
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        puts("Try again with an input");
        return -1;
    }
    int dimen = atoi(argv[1]);
    int size_win = atoi(argv[2]);
    nested_descend(dimen, size_win);

    return 0;
}
