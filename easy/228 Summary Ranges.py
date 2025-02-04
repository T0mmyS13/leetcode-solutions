class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if len(nums) == 1: # if there is only one element in the list
            return [str(nums[0])]
        if len(nums) == 0: # if the list is empty
            return []
        
        start = nums[0]
        output = []
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]: # if the next element is not part of the range
                if start == nums[i]:
                    output.append(str(start)) # add the single element to the output
                else:
                    output.append(str(start) + "->" + str(nums[i])) # add the range to the output
                start = nums[i+1]
        if start == nums[-1]: # if the last element is not part of the range
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(nums[-1])) # add the last range to the output
        return output

nums = [0, 1, 2, 4, 5, 7]
print(Solution().summaryRanges(nums)) # ["0->2","4->5","7"]

#time complexity: O(n)
#space complexity: O(1)

