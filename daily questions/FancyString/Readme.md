# 1957. Delete Characters to Make Fancy String

## Problem Description

A **fancy string** is a string where no three consecutive characters are equal.

Given a string `s`, delete the minimum possible number of characters from `s` to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

## Examples

### Example 1:
```
Input: s = "leeetcode"
Output: "leetcode"
Explanation: Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
```

### Example 2:
```
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation: Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
```

### Example 3:
```
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.

## Solution Approach

The solution uses a **greedy approach**:

1. Iterate through the string character by character
2. Keep track of consecutive character count
3. If we encounter the same character for the third consecutive time, skip it
4. Otherwise, add the character to the result

## My C# Solution

```csharp
public class Solution 
{
    public string MakeFancyString(string s) 
    {
        if (s.Length <= 2) return s;
        
        StringBuilder result = new StringBuilder();
        result.Append(s[0]);
        result.Append(s[1]);
        
        for (int i = 2; i < s.Length; i++)
        {
            // Only add current character if it doesn't create three consecutive same characters
            if (!(s[i] == result[result.Length - 1] && s[i] == result[result.Length - 2]))
            {
                result.Append(s[i]);
            }
        }
        
        return result.ToString();
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
        
        // Test Case 1
        string test1 = "leeetcode";
        string result1 = solution.MakeFancyString(test1);
        Console.WriteLine($"Input: \"{test1}\" -> Output: \"{result1}\""); 
        // Expected: "leetcode"
        
        // Test Case 2
        string test2 = "aaabaaaa";
        string result2 = solution.MakeFancyString(test2);
        Console.WriteLine($"Input: \"{test2}\" -> Output: \"{result2}\""); 
        // Expected: "aabaa"
        
        // Test Case 3
        string test3 = "aab";
        string result3 = solution.MakeFancyString(test3);
        Console.WriteLine($"Input: \"{test3}\" -> Output: \"{result3}\""); 
        // Expected: "aab"
        
        // Additional Test Case
        string test4 = "aaabbbbccccddeeeee";
        string result4 = solution.MakeFancyString(test4);
        Console.WriteLine($"Input: \"{test4}\" -> Output: \"{result4}\""); 
        // Expected: "aabbccddee"
    }
}
```

## Algorithm Walkthrough

Let's trace through Example 1: `s = "leeetcode"`

1. **i=0**: `'l'` - result = `"l"` (first character, always add)
2. **i=1**: `'e'` - result = `"le"` (second character, always add)
3. **i=2**: `'e'` - Check last two: `'l','e'` ≠ `'e','e'` → Add → result = `"lee"`
4. **i=3**: `'e'` - Check last two: `'e','e'` = `'e','e'` → Skip (would create 3 consecutive)
5. **i=4**: `'t'` - Check last two: `'e','e'` ≠ `'t','t'` → Add → result = `"leet"`
6. Continue similarly...

Final result: `"leetcode"`

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass through the string
- **Space Complexity**: O(n) - For the result string (StringBuilder/List)

## Key Insights

- We only need to check the last two characters to determine if adding the current character would create three consecutive identical characters
- This is a greedy problem where we can make the optimal choice at each step
- No backtracking is needed since we're minimizing deletions
- StringBuilder is more efficient than string concatenation for building the result