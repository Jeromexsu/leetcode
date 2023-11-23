def knapsack(weights, values, C):
    N = len(weights)
    dp = [[0]*(C+1) for _ in range(2)]
    # base case
    for c in range(C+1):
        if(c >= weights[0]) :
            dp[0][c] = values[0] 
    # iteration
    for i in range(1,N):
        for c in range(C+1):
            skip = dp[(i-1)&1][c]
            pick = 0
            if(c >= weights[i]):
                pick = dp[(i-1)&1][c-weights[i]] + values[i]
            dp[i&1][c] = max(skip,pick)
    return dp[(N-1)&1][C]

# driver code
weights = [4,2,3]
values = [4,2,3]
volume = 5
print(knapsack(weights,values,volume)) # 5 it is