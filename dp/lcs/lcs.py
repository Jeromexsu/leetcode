def _lcs(str1:str,str2:str,m,n):
    if m == 0 or n == 0: 
        return 0
    if str1[m-1] == str2[n-1]: 
        return 1+_lcs(str1,str2,m-1,n-1)
    return max(_lcs(str1,str2,m-1,n),_lcs(str1,str2,m,n-1))

def lcs(str1:str,str2:str):
    return _lcs(str1,str2,len(str1),len(str2))

S1 = "AGGTAB"
S2 = "GXTXAYB"

print(lcs(S1,S2))