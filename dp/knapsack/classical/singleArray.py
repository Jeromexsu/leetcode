def knapsack(weights, values, C):
    dp = [0]*(C+1)
    for i in range(len(weights)):
        for c in range(C,weights[i]-1,-1):
            pick = dp[c-weights[i]] + values[i]
            dp[c] = max(dp[c],pick)
    return dp[C]

# driver code
weights = [4,2,3]
values = [4,2,3]
volume = 5
print(knapsack(weights,values,volume)) # 5 it is