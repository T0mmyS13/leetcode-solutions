# 1277. Count Square Submatrices with All Ones

## Problem Description

Given a m x n matrix of ones and zeros, return how many square submatrices have all ones.

### Example 1:
```
Input: matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is 1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```

### Example 2:
```
Input: matrix = [[1,0,1],[1,1,0],[1,1,0]]
Output: 7
Explanation: 
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.
```

## Constraints
- 1 <= arr.length <= 300
- 1 <= arr[0].length <= 300
- 0 <= arr[i][j] <= 1

## Solution Approach
Use dynamic programming to count the number of square submatrices ending at each cell.

## C# Solution

```csharp
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
```

## Test Cases

```csharp
public class Program
{
    public static void Main(string[] args)
    {
        Solution solution = new Solution();
        int[][] test1 = new int[][] {
            new int[] {0,1,1,1},
            new int[] {1,1,1,1},
            new int[] {0,1,1,1}
        };
        Console.WriteLine(solution.CountSquares(test1)); // Expected: 15

        int[][] test2 = new int[][] {
            new int[] {1,0,1},
            new int[] {1,1,0},
            new int[] {1,1,0}
        };
        Console.WriteLine(solution.CountSquares(test2)); // Expected: 7
    }
}
```
