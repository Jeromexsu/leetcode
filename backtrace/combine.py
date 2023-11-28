def combine1(n,k):
    ans = []
    path = []
    def backtrace(i):
        d = k - len(path)
        if i < d: return
        if i == 0:
            if(len(path) == k):
                ans.append(path.copy())
            return
        #pick
        path.append(i)
        backtrace(i-1)
        path.pop()
        #skip
        backtrace(i-1)
    backtrace(n)
    print(ans)

def combine2(n,k):
    ans = []
    path = []
    def backtrace(i):
        d = k - len(path)
        if i < d: return
        if(len(path) == k):
            ans.append(path.copy())
        for j in range(i,0,-1):
            path.append(j)
            backtrace(j-1)
            path.pop()
    backtrace(n)
    print(ans)

combine2(4,2)
