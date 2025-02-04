class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
      
        min_price = float('inf')
        profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price
        return profit
    
# Time complexity: O(n)
# Space complexity: O(1)

prices = [7,1,5,3,6,4]

print(Solution().maxProfit(prices)) # 5