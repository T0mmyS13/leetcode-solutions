class ball:
    def __init__(self, number, color):
        self.number = number
        self.color = color

class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        balls=[]
        Output = []
        balls.append(ball(queries[0][0],queries[0][1]))
        for i in range(len(queries)):
            if all(queries[i][0] != b.number for b in balls):
                balls.append(ball(queries[i][0], queries[i][1]))
            else:
                for j in range(len(balls)):
                    if balls[j].number == queries[i][0]:
                        balls[j].color = queries[i][1]
            unique_colors = {ball.color for ball in balls}
            Output.append(len(unique_colors))
        return Output
    
# Time complexity: O(n^2)   funguje to, ale je to pomale
# Space complexity: O(n)    

print(Solution().queryResults(4,[[1,4],[2,5],[1,3],[3,4]])) # [1, 2, 2, 3]
            

                

        

        


            