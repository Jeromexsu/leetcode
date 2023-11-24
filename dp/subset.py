# Given a set of non-negative integers and a value sum, 
# the task is to check if there is a subset of the given set 
# whose sum is equal to the given sum. 

# pick = f(i-1,c-costs[i])
# f(i,c) = f(i-1,c) || pick
def subset(costs,constraint):
    dp = [False] * (constraint + 1)
    dp[0] = True
    for i in range(len(costs)):
        for c in range(constraint,costs[i]-1,-1):
            dp[c] = dp[c] or dp[c-costs[i]]
    return dp[constraint]

set = [3, 34, 4, 12, 5, 2]
sum = 9
print(subset(set,sum))