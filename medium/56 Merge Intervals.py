class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals,key=lambda x:x[0]) #sort the intervals based on the start of the interval
        if len(intervals)==0:
            return []
        if len(intervals)==1:
            return intervals
        
        output=[]
        output.append(intervals[0]) 
        for i in range(1,len(intervals)):
            if  output[-1][1]<=intervals[i][1] and intervals[i][0]<=output[-1][1]: # if the end of the previous interval is less than or equal to the end of the next interval and the start of the next interval is less than or equal to the end of the previous interval
                output[-1][1]=intervals[i][1]
            elif output[-1][1]>=intervals[i][1] and intervals[i][0]>=output[-1][0]: # if the end of the previous interval is greater than or equal to the end of the next interval and the start of the next interval is greater than or equal to the start of the previous interval
                output[-1][1]=output[-1][1]
            else:
                output.append(intervals[i])
        return output

#time complexity is O(nlogn) because of sorting
#space complexity is O(n) because of the output array
    
intervals = [[1,3],[2,6],[8,10],[15,18]] #[[1, 6], [8, 10], [15, 18]]
print(Solution().merge(intervals))

               