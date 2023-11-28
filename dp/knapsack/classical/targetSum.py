def targetSum(nums,target): 
    n = len(nums)
    dp = [[0]*(target+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1,n+1):
        num = nums[i-1]
        for c in range(target+1):
            if c < num: dp[i][c] = dp[i-1][c]
            else : dp[i][c] = dp[i-1][c] + dp[i-1][c-num]
    return dp[n][target]

    # def backtrace(i,c): # 考虑前i个数，和为c的方案数
    #     if i < 0: 
    #         return 1 if c == 0 else 0
    #     if c < nums[i]: return backtrace(i-1,c)
    #     return backtrace(i-1,c)+backtrace(i-1,c-nums[i])
    # return backtrace(len(nums)-1,target)

nums = [1,1,1,1]
target = 3
print(targetSum(nums,target))