#include <stdio.h>

int a = 5;


int fun() {
    a = 17;
    return 3;
}

int main(int argc, char **argv) {
    a = a + fun();
    printf("This is 'a': %d\n", a);
    
    return 0;
}
