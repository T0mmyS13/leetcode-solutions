public class Solution
{
    public int[][] SortMatrix(int[][] grid)
    {
        int n = grid.Length;
        for (int i = 0; i < n; i++)
        {


        }

    }
}
public class Program
{
    public void Main(string[] args)
    {
        Solution s = new Solution();
        int[][] grid = [[1, 7, 3], [9, 8, 2], [4, 5, 6]];
        int[][] result = s.SortMatrix(grid);
        Console.WriteLine(result);
        
    }
        
}

