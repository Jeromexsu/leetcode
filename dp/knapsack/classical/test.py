def lengthOfLongestSubsequence(nums, target: int) -> int:
    n = len(nums)
    dp = [[0]*(target+1) for _ in range(n+1)]
    for c in range(target+1):
        dp[0][c] = 0 if c == 0 else -float('inf')
    for i in range(1,n+1):
        x = nums[i-1]
        for c in range(target+1):
            if c < nums[i]: dp[i][c] = dp[i-1][c]
            else: dp[i][c] = max(dp[i-1][c-x],dp[i-1][c])
    if dp[n][target] == -float('inf'): return -1
    return dp[n][target]

print(lengthOfLongestSubsequence([1,2,3,4,5],9))