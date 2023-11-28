# 给定一个不含重复数字的数组 nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案。

def permute(nums):
    n = len(nums)
    ans = []
    path = [0]*n
    
    def backtrace(i,s):
        if i == n:
            ans.append(path.copy())
        for x in s:
            path[i] = x
            backtrace(i+1,s-{x})
    
    backtrace(0,set(nums))
    return ans

print(permute([1,2,3,4]))