class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        close=(nums[0])
        for num in nums:
            if num == 0:
                return num
            elif abs(num)<abs(close):
                close=num
            elif abs(num)==abs(close) and num>close:
                close=num
        return close
    
# Time complexity: O(n)
# Space complexity: O(1)

nums = [-1, 2, 1, -4]
print(Solution().findClosestNumber(nums)) # 1
