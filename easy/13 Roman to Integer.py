class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        arabic = [0] * len(s)
        for  i in range(len(s)):
            if s[i] == 'I':
                arabic[i] = 1
            elif s[i] == 'V':
                arabic[i] = 5
            elif s[i] == 'X':
                arabic[i] = 10
            elif s[i] == 'L':
                arabic[i] = 50
            elif s[i] == 'C':
                arabic[i] = 100
            elif s[i] == 'D':
                arabic[i] = 500
            elif s[i] == 'M':
                arabic[i] = 1000

        result = 0
        for i in range(len(arabic) - 1): 
            if arabic[i] < arabic[i + 1]:
                result -= arabic[i]
            else:
                result += arabic[i]
        result += arabic[-1]
        return result
    
# Time complexity: O(n)
# Space complexity: O(n)

print(Solution().romanToInt('LVIII')) # 58

