class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=0 #initialize the max_sum to 0
        posible_max=nums[0] #initialize the posible_max to the first element in the array
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]: #if the current number is greater than or equal to the previous number
                posible_max+=nums[i]
            elif posible_max>max_sum: #if the posible_max is greater than the max_sum
                max_sum=posible_max
                posible_max=nums[i]
            else:
                posible_max=nums[i]
        return max(max_sum,posible_max) 
    
#time complexity is O(n) because we are iterating through the array once
#space complexity id O(1) because we are not using any extra space

nums = [10,20,30,5,10,50] #65
print(Solution().maxAscendingSum(nums))