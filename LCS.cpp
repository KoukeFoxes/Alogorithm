#include "/Users/doeshing/development/stdc++.h"

using namespace std;

int LCS(string x, string y)
{
  int m = x.length();
  int n = y.length();
  int dp[m + 1][n + 1];
  string label[m + 1][n + 1];

  for (int i = 0; i <= m; i++)
  {
    for (int j = 0; j <= n; j++)
    {
      if (i == 0 || j == 0)
      {
        dp[i][j] = 0;
        label[i][j] = "";
      }
      else if (x[i - 1] == y[j - 1])
      {
        dp[i][j] = dp[i - 1][j - 1] + 1;
        label[i][j] = "\\";
      }
      else
      {
        if (dp[i - 1][j] >= dp[i][j - 1])
        {
          dp[i][j] = dp[i - 1][j];
          label[i][j] = "^";
        }
        else
        {
          dp[i][j] = dp[i][j - 1];
          label[i][j] = "<";
        }
      }
    }
  }

  for (int i = n; i > 0; i--)
  {

    if (dp[m][i] == dp[m][n])
    {
      stack<char> result;
      int control_X = i;
      int control_Y = m;

      while (control_X != 0 && control_Y != 0)
      {
        if (label[control_Y][control_X] == "\\")
        {
          result.push(y[control_X - 1]);
          // cout << "X:" << control_X << " "
          //      << "Y:" << control_Y << endl;
          control_X--;
          control_Y--;
        }
        else if (label[control_Y][control_X] == "^")
        {
          control_Y--;
        }
        else if (label[control_Y][control_X] == "<")
        {
          control_X--;
        }
      }

      while (!result.empty())
      {
        cout << result.top();
        result.pop();
      }
      cout << endl;
    }
  }
  return dp[m][n];
}

int main()
{
  string x, y;
  // cin >> x >> y;
  x = "ABCBDAB";
  y = "BDCABA";
  cout << LCS(x, y) << endl;
}