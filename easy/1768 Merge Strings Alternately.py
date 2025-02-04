class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        for i in range(min(len(word1), len(word2))):
            merged.append(word1[i])
            merged.append(word2[i])
        
        if len(word1) > len(word2):
            merged.extend(word1[len(word2):])
        else:
            merged.extend(word2[len(word1):])
        
        return ''.join(merged)
    
# Time complexity: O(n)
# Space complexity: O(n)

word1 = "abc"
word2 = "pqr"
print(Solution().mergeAlternately(word1, word2)) # apbqcr