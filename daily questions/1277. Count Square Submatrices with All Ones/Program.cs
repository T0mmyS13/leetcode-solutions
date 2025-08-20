using System;


public class Solution
{
    public int CountSquares(int[][] matrix)
    {
        int squares = 0;

        int m = matrix.Length, n = matrix[0].Length;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (matrix[i][j] == 1)
                {
                    squares++;
                }
                if (i > 0 && j > 0 && matrix[i][j] == 1)
                {
                    // Check the minimum of the three neighbors
                    matrix[i][j] = Math.Min(Math.Min(matrix[i - 1][j], matrix[i][j - 1]), matrix[i - 1][j - 1]) + 1;
                    squares += matrix[i][j] - 1; // Add the number of new squares formed
                }
            }
        }
        return squares;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Solution solution = new Solution();
        int[][] test1 = new int[][] {
            new int[] {0,1,1,1},
            new int[] {1,1,1,1},
            new int[] {0,1,1,1}
        };
        Console.WriteLine($"Test 1 Output: {solution.CountSquares(test1)}"); // Expected: 15

        int[][] test2 = new int[][] {
            new int[] {1,0,1},
            new int[] {1,1,0},
            new int[] {1,1,0}
        };
        Console.WriteLine($"Test 2 Output: {solution.CountSquares(test2)}"); // Expected: 7
    }
}
