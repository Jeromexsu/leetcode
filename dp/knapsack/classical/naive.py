# Given N items where each item has some weight and profit associated with it 
# and also given a bag with capacity W. 
# The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible. 
 
def knapsack(weights, values, C):
    N = len(weights)
    dp = [[0]*(C+1) for _ in range(N)]
    # base case
    for c in range(C+1):
        if(c >= weights[0]) :
            dp[0][c] = values[0] 
    # iteration
    for i in range(1,N):
        for c in range(C+1):
            skip = dp[i-1][c]
            pick = 0
            if(c >= weights[i]):
                pick = dp[i-1][c-weights[i]] + values[i]
            dp[i][c] = max(skip,pick)
    return dp[N-1][C]

# driver code
weights = [4,2,3]
values = [4,2,3]
volume = 5
print(knapsack(weights,values,volume)) # 5 it is

