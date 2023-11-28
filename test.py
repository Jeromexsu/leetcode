# 1230 -> 1,2,3,0, 
# f(i)
# 1 / 2,3,0,
# 100 1,00
def splitAll(num:int):
    numstr = str(num)
    n = len(numstr)
    ans = []
    path = []

    def backtrace(i,start):
        if i == n:
            ans.append(path.copy())
            return 
        #skip
        if i < n-1:
            backtrace(i+1,start)
        #pick
        path.append(numstr[start:i+1])
        backtrace(i+1,i+1)
        path.pop()
    backtrace(0,0)
    print(ans)

splitAll(1234)



