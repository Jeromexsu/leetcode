def _lcs(str1,str2,m,n,dp):
    if dp[m][n] != -1 : 
        return dp[m][n]
    if m == 0 or n == 0: 
        dp[m][n] = 0
        return dp[m][n]
    elif str1[m-1] == str2[n-1]: 
        dp[m][n] = _lcs(str1,str2,m-1,n-1,dp)+1
        return dp[m][n]
    else :
        return max(_lcs(str1,str2,m-1,n,dp),_lcs(str1,str2,m,n-1,dp))

def lcs(str1,str2): 
    m = len(str1)
    n = len(str2)
    dp = [[-1]*(n+1) for _ in range(m+1)]
    return _lcs(str1,str2,len(str1),len(str2),dp)

S1 = "AGGTAB"
S2 = "GXTXAYB"
print(lcs(S1,S2))
