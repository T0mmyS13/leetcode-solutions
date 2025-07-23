public class Solution
{
    public int MaximumGain(string s, int x, int y)
    {
        // Determine which pattern to prioritize (higher score first)
        string first = x >= y ? "ab" : "ba";
        string second = x >= y ? "ba" : "ab";
        int firstScore = x >= y ? x : y;
        int secondScore = x >= y ? y : x;
        
        // First pass: remove the higher-scoring pattern
        string afterFirst = RemovePattern(s, first, firstScore, out int score1);
        
        // Second pass: remove the remaining pattern
        string afterSecond = RemovePattern(afterFirst, second, secondScore, out int score2);
        
        return score1 + score2;
    }
    
    private string RemovePattern(string s, string pattern, int score, out int totalScore)
    {
        totalScore = 0;
        var stack = new List<char>();
        
        foreach (char c in s)
        {
            stack.Add(c);
            
            // Check if we can form the pattern with the last two characters
            if (stack.Count >= 2 && 
                stack[stack.Count - 2] == pattern[0] && 
                stack[stack.Count - 1] == pattern[1])
            {
                // Remove the pattern (last two characters)
                stack.RemoveAt(stack.Count - 1);
                stack.RemoveAt(stack.Count - 1);
                totalScore += score;
            }
        }
        
        return new string(stack.ToArray());
    }
}

// Time: O(n) - single pass through the string for each pattern
// Space: O(n) - stack space for processing characters

public class Program
{
    public static void Main(string[] args)
    {
        Solution solution = new Solution();
        string s = "cdbcbbaaabab";
        int x = 4, y = 5;
        int result = solution.MaximumGain(s, x, y);
        Console.WriteLine($"Maximum Gain: {result}"); // Output: 19

        // Test with another example
        string s2 = "aabbaaxybbaabb";
        int x2 = 5, y2 = 4;
        int result2 = solution.MaximumGain(s2, x2, y2);
        Console.WriteLine($"Second test case result: {result2}"); // Output: 5
    }
}