def maxProfit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit
  
'''
Time complexity: O(n). It iterates through the array only once.
Space complexity: O(1), which is constant. The solution only uses a constant amount of extra space to store the minimum price seen so far and the maximum profit that can be made by selling the stock.

Things I kept in mind:
1) Check if there is any possibility of making a profit before calculating the maximum profit. If there is no profit, the function should return 0.
2) In some cases, the profit obtained from buying and selling the stock can be negative. 
'''
