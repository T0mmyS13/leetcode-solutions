class Solution(object):
    def maxNumberOfBalloons(self, text) -> int:
        """
        :type text: str
        :rtype: int
        """
        b=text.count('b')
        a=text.count('a')
        l=text.count('l')//2
        o=text.count('o')//2
        n=text.count('n')
        return min(b,a,l,o,n)

# Time Complexity: O(n)
# Space Complexity: O(1)


# Example usage
text = "nlaebolko"
print(Solution().maxNumberOfBalloons(text))  # Output: 1

