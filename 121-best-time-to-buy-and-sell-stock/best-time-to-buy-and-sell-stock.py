class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = sys.maxsize-1
        profit = 0
        for i in range(len(prices)):
            if mini > prices[i]:
                mini = prices[i]
            profit = max(profit,prices[i]-mini)
        return profit


        # profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if (prices[j]>prices[i]):
        #             profit = max(profit,prices[j]-prices[i])
        # return profit




        # first_low = sys.maxsize-1
        # k =0
        # for i in range(k,len(prices)):
            
        #     if first_low>prices[i]:
        #         k=i
        #         first_low = prices[i]
        #         if k ==len(prices)-1:
        #             return 0
                
        # for j in range(k,len(prices)):
        #     maxx = max(prices[k:len(prices)+1])
        # return maxx-first_low
            

