def maxProfit(prices) -> int:
    hold = True
    def f(i,status):
        if i == 0:
            return -prices[0] if status == hold else 0
        if status == hold:
            return max(f(i-1,hold),f(i-1,not hold)-prices[i])
        else: return max(f(i-1, not hold), f(i-1,hold)+ prices[i])
    return f(len(prices)-1,not hold)