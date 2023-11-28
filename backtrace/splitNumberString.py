def splitNumber(number):
    ans = []
    path = []
    num = str(number)
    n = len(num)
    def backtrace(i):
        if i == n:
            ans.append(path.copy())
            return
        for j in range(i,n):
            sub = num[i:j+1]
            path.append(sub)
            backtrace(j+1)
            path.pop()
            if sub == '0': break
    backtrace(0)
    print(ans)
splitNumber(1024)

