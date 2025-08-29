class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countednumbers = {}
        for num in nums:
            if num in countednumbers:
                countednumbers[num] += 1
            else:
                countednumbers[num] = 1
        return max(countednumbers, key=countednumbers.get)
