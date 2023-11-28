def maxProfit(prices) -> int:
    n = len(prices)
    hold = 0
    notHold = 1
    dp = [[0] * 2 for _ in range(n)]
    dp[0][hold] = -prices[0]
    dp[0][notHold] = 0
    for i in range(1,n):
        dp[i][hold] = max(dp[i-1][hold],dp[i-1][notHold]-prices[i])
        dp[i][notHold] = max(dp[i-1][notHold],dp[i-1][hold]+prices[i])
    return dp[n-1][notHold]