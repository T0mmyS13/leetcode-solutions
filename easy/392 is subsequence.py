class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if t[i] == s[0]:
                s = s[1:]  # remove the first character of s
                if len(s) == 0:
                    return True
        
        return False

# Time complexity: O(n)
# Space complexity: O(1)



s = "abc"
t = "ahbgdc"

print(Solution().isSubsequence(s, t)) # True