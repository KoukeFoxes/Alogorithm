#include <stdio.h>

int gcd(int x, int y) {
    return x ? gcd(y % x, x) : y; // if x is 0 , return y
}
int main(void) {
  printf("%d", gcd(169,39));
  return 0;
}
