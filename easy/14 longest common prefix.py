class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for char in min(strs):
            for i in range(len(strs)):
                if strs[i][0] != char:
                    return prefix
                else:
                    strs[i] = strs[i][1:]
            prefix += char
        
        return prefix
        
            
strs=["flower","flow","flight"] 
print(Solution().longestCommonPrefix(strs)) # "fl"    