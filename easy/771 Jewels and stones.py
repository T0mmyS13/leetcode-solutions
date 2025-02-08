class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels_set = set(jewels) # set of jewels
        count = 0 
        for stone in stones: # iterate through stones
            if stone in jewels_set: # if the stone is a jewel
                count += 1
        return count
        
    
# Time complexity: O(n)
# Space complexity: O(1)

print(Solution().numJewelsInStones("aA", "aAAbbbb")) # 3