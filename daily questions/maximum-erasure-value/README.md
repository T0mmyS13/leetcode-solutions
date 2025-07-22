# Maximum Erasure Value

## Problem Description

Given an array of positive integers `nums`, return the **maximum** sum of elements in a subarray where all elements are **unique**.

A subarray is a contiguous sequence of elements within an array.

### Examples

**Example 1:**
```
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
```

**Example 2:**
```
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
```

## Solution Approach

This solution uses the **Sliding Window** technique with a **HashSet** to efficiently find the maximum sum subarray with unique elements.

### Algorithm Steps

1. **Initialize**: Set up two pointers (`left`, `right`), a running sum (`currentSum`), and a HashSet to track unique elements
2. **Expand Window**: Move the `right` pointer and add elements to the current sum
3. **Handle Duplicates**: When a duplicate is found, shrink the window from the left until the duplicate is removed
4. **Track Maximum**: Keep track of the maximum sum encountered

## Complexity Analysis

- **Time Complexity**: O(n) - Each element is visited at most twice
- **Space Complexity**: O(min(n, k)) where k is the number of unique elements

## Code Structure

```csharp
public class Solution
{
    public int MaximumUniqueSubarray(int[] nums)
    {
        // Optimized sliding window implementation
        // Uses incremental sum calculation for better performance
    }
}
```

## How to Run

### Prerequisites
- .NET 9.0 or later
- Visual Studio Code or Visual Studio

### Build and Run
```bash
# Navigate to project directory
cd "daily questions/maximum-erasure-value"

# Build the project
dotnet build

# Run the project
dotnet run
```

### Expected Output
```
Maximum Unique Subarray Sum: 17
Second test case result: 8
```

## Performance Features

✅ **Optimized Memory Usage** - No additional arrays needed  
✅ **Fast Execution** - Direct arithmetic operations instead of array lookups  
✅ **Cache Friendly** - Minimal memory access patterns  
✅ **Single Pass** - O(n) time complexity with good constant factors  

## Test Cases

The solution includes two test cases:

1. **Test Case 1**: `[4, 2, 4, 5, 6]` → Expected: `17`
   - Optimal subarray: `[2, 4, 5, 6]`

2. **Test Case 2**: `[5, 2, 1, 2, 5, 2, 1, 2, 5]` → Expected: `8`
   - Optimal subarray: `[5, 2, 1]` or `[1, 2, 5]`

## Algorithm Visualization

For array `[4, 2, 4, 5, 6]`:

| Step | Window | Sum | Max Sum | Action |
|------|--------|-----|---------|---------|
| 1 | [4] | 4 | 4 | Add 4 |
| 2 | [4, 2] | 6 | 6 | Add 2 |
| 3 | [2, 4] | 6 | 6 | Remove first 4, add second 4 |
| 4 | [2, 4, 5] | 11 | 11 | Add 5 |
| 5 | [2, 4, 5, 6] | 17 | **17** | Add 6 |

## Related Problems

- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

## Tags

`Array` `Hash Table` `Sliding Window` `Optimization` `LeetCode`
