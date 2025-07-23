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

## Algorithm

```python
def makeFancyString(s: str) -> str:
    result = []
    
    for char in s:
        # If we have less than 2 characters or the current character
        # is different from the last two, we can safely add it
        if len(result) < 2 or not (result[-1] == result[-2] == char):
            result.append(char)
    
    return ''.join(result)
```

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass through the string
- **Space Complexity**: O(n) - For the result string

## Key Insights

- We only need to check the last two characters to determine if adding the current character would create three consecutive identical characters
- This is a greedy problem where we can make the optimal choice at each step
- No backtracking is needed since we're minimizing deletions