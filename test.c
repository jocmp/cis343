#include <stdio.h>

int main() {
    int x[3][4] = { 0 };
    int rows = 3;
    int columns = 4;
    int counter = 1;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            x[i][j] = counter;
            counter++;
        }
    }
    // Diagonally left-down
    for (int slice = 0; slice < rows + columns - 1; ++slice) {
        printf("Slice %d: ", slice);
        int skip_end = slice < columns ? 0: slice - columns + 1;
        int skip_start = slice < rows ? 0 : slice - rows + 1;
        for (int j = slice - skip_start; j >= skip_end; --j) {
            printf("%d ", x[j][slice - j]);
        }
        printf("\n");
    }
    // Diagonally up-right
    for (int slice = 0; slice < rows + columns - 1; ++slice) {
        printf("Slice %d: ", slice);
        int skip_end = slice < columns ? 0: slice - columns + 1;
        int skip_start = slice < rows ? 0 : slice - rows + 1;
        for (int j = slice - skip_start; j >= skip_end; --j) {
            printf("%d ", x[rows - j - 1][slice - j]);
        }
        printf("\n");
    }
    return 0;
}
