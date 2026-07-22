class Solution(object):
    def maxProfit(self, prices):
        #use the two pointers
        buy = 0
        sell = 1
        maxP = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            else:
                buy = sell
            sell += 1
        return maxP


        