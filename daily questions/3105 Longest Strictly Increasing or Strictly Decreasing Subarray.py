class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: 
            return 0
        if len(nums) == 1:
            return 1
        subarraydown = [nums[0]]
        subarrayup = [nums[0]]
        long_subarray = []
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if len(subarraydown) > len(long_subarray):
                    long_subarray = subarraydown
                subarraydown= []
                subarrayup.append(nums[i])
            elif nums[i] < nums[i - 1]:
                if len(subarrayup) > len(long_subarray):
                    long_subarray = subarrayup
                subarrayup=[]
                subarraydown.append(nums[i])
            
        return max(1,len(long_subarray), len(subarrayup), len(subarraydown))

nums = [1,9,7,1] 
print(Solution().longestMonotonicSubarray(nums))  #not working for this case need to fix it later  

                