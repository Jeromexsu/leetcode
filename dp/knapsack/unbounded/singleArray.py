def boundedKnapsack(costs,values,constrain):
    dp = [0]*(constrain+1)
    for i in range(len(costs)):
        for c in range(costs[i],constrain+1):
            pick = dp[c-costs[i]]+values[i]
            dp[c] = max(dp[c],pick)
    return dp[constrain]

costs = [1,50]
values = [1,30]
constrain = 100
print(boundedKnapsack(costs,values,constrain))

values = [10, 40, 50, 70]
costs = [1, 3, 4, 5]
constrain = 8
print(boundedKnapsack(costs,values,constrain))
