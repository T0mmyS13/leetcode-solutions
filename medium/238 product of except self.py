class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            self = nums[i]
            nums.remove(nums[i])
            output.append(multiply_list(nums))
            nums.insert(i, self)
        return output

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

#time complexity: O(n^2)  suppose to be O(n) need to fix this
#space complexity: O(n)

nums = [1,2,3,4]
print(Solution().productExceptSelf(nums)) # [24,12,8,6]