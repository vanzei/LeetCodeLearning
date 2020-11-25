class Solution:
    def maxProfit(self, prices):
        buy_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < buy_price:
                buy_price = price
            elif price - buy_price > max_profit:
                max_profit = price - buy_price
        return(max_profit)


test1=Solution()
print(test1.maxProfit([7,1,5,3,6,4]))

test2=Solution()
print(test2.maxProfit([7,6,4,3,1]))  