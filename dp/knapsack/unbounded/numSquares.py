def numSquares(n: int) -> int:
    def squares(n):
        arr = []
        for i in range(n+1):
            if(i*i <= n):
                arr.append(i*i)
            else: break
        return arr
    print(squares(n))
    def knapsack(costs,constraint):
        N = len(costs)
        dp = [float('inf')] * (constraint+1)
        dp[0] = 0
        for i in range(1,N+1):
            cur = costs[i-1]
            for c in range(constraint+1):
                skip = dp[c]
                pick = float('inf')
                if(c >= cur and dp[c-cur] != float('inf')):
                    pick = dp[c-cur] + 1
                dp[c] = min(skip,pick)
        return dp[constraint]
    print(knapsack(squares(n),n))
                
numSquares(2194)
