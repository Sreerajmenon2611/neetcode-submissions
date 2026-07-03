class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[0 for i in range(len(prices))]
        dp[-1]=prices[-1]
        for i in range(len(prices)-2,-1,-1):
            dp[i]=max(dp[i+1],prices[i+1])
        for i in range(len(dp)):
            dp[i]=dp[i]-prices[i]
        if max(dp)<=0:
            return 0
        return max(dp)
        