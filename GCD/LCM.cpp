#include "/Users/doeshing/development/stdc++.h"
using namespace std;

// gcd
int gcd(int a, int b)
{
    return b ? gcd(b, a % b) : a;
}

// lcm
int lcm(int a, int b)
{
    return a * b / gcd(a, b);
}
