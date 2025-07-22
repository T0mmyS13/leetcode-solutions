using System;
using System.Collections.Generic;

public class Solution
{
    public int MaximumUniqueSubarray(int[] nums)
    {
        int maxSum = 0;
        int currentSum = 0;
        int left = 0;
        HashSet<int> seen = new HashSet<int>();

        for (int right = 0; right < nums.Length; right++)
        {
            // Add current element to sum
            currentSum += nums[right];
            
            // Remove duplicates from left side
            while (seen.Contains(nums[right]))
            {
                seen.Remove(nums[left]);
                currentSum -= nums[left];
                left++;
            }
            
            // Add current element to seen set
            seen.Add(nums[right]);
            
            // Update maximum sum
            maxSum = Math.Max(maxSum, currentSum);
        }

        return maxSum;
    }
}

// Time: O(n) - each element is visited at most twice
// Space: O(min(n, k)) where k is the number of unique elements
public class Program
{
    public static void Main(string[] args)
    {
        Solution solution = new Solution();
        int[] nums = { 4, 2, 4, 5, 6 };
        int result = solution.MaximumUniqueSubarray(nums);
        Console.WriteLine($"Maximum Unique Subarray Sum: {result}"); // Output: 17

        // Test with another example
        int[] nums2 = { 5, 2, 1, 2, 5, 2, 1, 2, 5 };
        int result2 = solution.MaximumUniqueSubarray(nums2);
        Console.WriteLine($"Second test case result: {result2}"); // Output: 8
    }
}
