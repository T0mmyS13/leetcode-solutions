class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
            
        for char in t:
            if char in chars:
                chars[char] -= 1
                if chars[char] == 0:
                    del chars[char]
            else:
                return False
        return len(chars) == 0
    
#Time Complexity: O(n)
#Space Complexity: O(n)

# Example usage
s = "aacc"
t = "ccaa"
print(Solution().isAnagram(s, t))  # Output: True