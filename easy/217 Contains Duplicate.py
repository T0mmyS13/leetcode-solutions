class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) # if the length of the list is not equal to the length of the set, there are duplicates
    
# Time complexity: O(n)
# Space complexity: O(n)

print(Solution().containsDuplicate([1,2,3,1])) # True