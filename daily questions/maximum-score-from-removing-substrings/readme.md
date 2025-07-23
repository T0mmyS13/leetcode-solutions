# 1717. Maximum Score From Removing Substrings

## Problem Description

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times:

- Remove substring `"ab"` and gain `x` points.
- Remove substring `"ba"` and gain `y` points.

Return the maximum points you can gain after applying the above operations on `s`.

## Examples

### Example 1:
```
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
```

### Example 2:
```
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
```

## Constraints

- `1 <= s.length <= 10^5`
- `1 <= x, y <= 10^4`
- `s` consists of lowercase English letters.

## Solution Approach

This problem requires a **greedy strategy with two-pass stack algorithm**:

### Key Insight
To maximize points, we should prioritize removing the substring that gives more points first. This is because removing one pattern might create opportunities for the other pattern.

### Algorithm Steps

1. **Determine Priority**: Compare `x` and `y` to decide which pattern (`"ab"` or `"ba"`) to remove first
2. **First Pass**: Use a stack to greedily remove all instances of the higher-scoring pattern
3. **Second Pass**: Use another stack to remove all instances of the remaining pattern from the leftover string

### Implementation Details

```csharp
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
```

### Stack-Based Pattern Removal

```csharp
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
```

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass through the string for each pattern (2 passes total)
- **Space Complexity**: O(n) - Stack space for processing characters

## Why This Approach Works

1. **Greedy Choice**: Always removing the higher-scoring pattern first maximizes the total score
2. **Stack Efficiency**: The stack allows us to detect and remove patterns in O(1) time as we encounter them
3. **Optimal Substructure**: The choice of which pattern to prioritize doesn't depend on future characters

## Alternative Approaches

- **Naive Approach**: Repeatedly search and remove substrings - O(n²) time complexity
- **Dynamic Programming**: Overkill for this problem and less efficient than the greedy approach

## Test Cases

```csharp
// Test Case 1
string s1 = "cdbcbbaaabab";
int x1 = 4, y1 = 5;
// Expected: 19

// Test Case 2  
string s2 = "aabbaaxybbaabb";
int x2 = 5, y2 = 4;
// Expected: 20
```