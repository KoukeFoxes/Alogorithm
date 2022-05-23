import java.util.Scanner;

public class temp{
    public static void main(String[] args) {
        var scn = new Scanner(System.in);
        int n = scn.nextInt();
        
        // fibonacci number with matrix multiplication
        System.out.println(fib(n));
    }

    // multiply matrix by matrix
    public static int[][] multiply(int[][] a, int[][] b) {
        int[][] c = new int[a.length][b[0].length];
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < b[0].length; j++) {
                for (int k = 0; k < a[0].length; k++) {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return c;
    }

    // calaculate power of matrix
    public static int[][] power(int[][] a, int n) {
        if (n == 1) {
            return a;
        }
        int[][] b = power(a, n / 2);
        b = multiply(b, b);
        if (n % 2 == 1) {
            b = multiply(b, a);
        }
        return b;
    }

    //fib(n) = A^(n-1)[0][0]
    public static int fib(int n) {
        int[][] a = {{1, 1}, {1, 0}};
        int[][] b = power(a, n - 1);
        return b[0][0];
    }

    
}
