from typing import List


def maxProfit(prices):
    pass


print(maxProfit([3, 2, 6, 5, 0, 3]))
print(maxProfit([2, 3, 6, 5, 0, 3]))


# [3, 2, 6, 5, 0, 3] # 4
def maxProfit(prices: List[int]) -> int:
    # Solution 3
    p = 0
    buy, sell = 0, 1
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            p = max(prices[sell] - prices[buy], p)
        else:
            buy = sell
        sell += 1
    return p

    # Solution 2
    profit = 0
    bought_at = prices[0]
    sold_at = 0
    i = 0
    while i < len(prices) - 1:
        if prices[i] < prices[i + 1] and prices[i] < bought_at:
            bought_at = prices[i]
            sold_at = max(prices[i:])
            if sold_at - bought_at > profit:
                profit = sold_at - bought_at
        i += 1
    return profit

    # Solution 1
    profit = 0
    i = 0
    while i < len(prices) - 1:
        j = len(prices) - 1
        while i < j:
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
            j -= 1
        i += 1
    return profit


# print(maxProfit([7, 1, 5, 3, 6, 4]))  # 5
# print(maxProfit([7, 6, 4, 3, 1]))  # 0
print(maxProfit([3, 2, 6, 5, 0, 3]))  # 4
