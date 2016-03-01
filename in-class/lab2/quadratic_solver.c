#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define POSITIVE 1
#define NEGATIVE 0

float solve_quad(float a, float b, float c, int positive) {
    // Solve for x
    float x;
    x = sqrtf(powf(b, 2) - 4 * a * c);
    if(positive) {
       x = -b + x;
    } else {
       x = -b - x;
    }
    return x / (2 * a);
}

int main(int argc, char* argv[]) {
  float a, b, c;
  float answer_pos, answer_neg;
  // Check if A, B, C are passed in 
  // as arguments
  if(argc < 4) {
    // If not, prompt user
    printf("Enter A: ");
    scanf("%f", &a);
    printf("Enter B: ");
    scanf("%f", &b);
    printf("Enter C: ");
    scanf("%f", &c);
  } else {
    // If so, convert arguments to floats
    a = atof(argv[1]);
    b = atof(argv[2]);
    c = atof(argv[3]);
  }

  // We need to check both the positive value
  // of x and the negative value.
  answer_pos = solve_quad(a, b, c, POSITIVE);
  answer_neg = solve_quad(a, b, c, NEGATIVE);

  // Print out results
  printf("x = %f\n", answer_pos);
  printf("x = %f\n", answer_neg);

  return 0;
}

