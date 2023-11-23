def knapsack(weights, values, C):
    N = len(weights)
    dp = [0]*(C+1)
    for i in range(N):
        for c in range(C,weights[i]-1,-1):
            skip = dp[c]
            pick = dp[c-weights[i]] + values[i]
            dp[c] = max(skip,pick)
    return dp[C]

# driver code
weights = [4,2,3]
values = [4,2,3]
volume = 5
print(knapsack(weights,values,volume)) # 5 it is