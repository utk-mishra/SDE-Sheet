def maxProfit(self, prices: List[int]) -> int:    
    # keep updating minPrice and check against the current element - simple af
    maxProfit = 0
    minPrice = float("inf")
    for p in prices:
        if p < minPrice:
            minPrice = p
        else:
            profit = p - minPrice
            maxProfit = max(profit, maxProfit)
    return maxProfit
    
    # time - O(n)
    # space - O(1)