# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #APPROACH 1
        # mini=prices[0]
        # max_profit=0
        # for i in range(1,len(prices)):
        #     profit=prices[i]-mini
        #     max_profit=max(max_profit,profit)
        #     mini=min(mini,prices[i])
        # return max_profit


        #APPROACH 2
        # l,r=0,1
        # max_profit=0
        # while r<len(prices):
        #     if prices[l]<prices[r]:
        #         max_profit=max(max_profit,prices[r]-prices[l])
        #     else:
        #         l=r
        #     r+=1
        # return max_profit


        #APPROACH 3
        if not prices:
            return 0
        max_profit, lowest_price, highest_price = 0, prices[0], prices[0]
        for price in prices:
            if price < lowest_price:
                lowest_price = price
                highest_price = price
            elif price > highest_price:
                max_profit = max(max_profit, price - lowest_price)
                highest_price = price
        return max_profit
