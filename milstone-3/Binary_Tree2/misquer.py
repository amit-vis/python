import sys,math
def minSqueres(n, dp):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root+1):
        newcheckvalue = n-(i**2)
        if dp[newcheckvalue] == -1:
            smallAns = minSqueres(newcheckvalue,dp)
            dp[newcheckvalue] = smallAns
            currAns =1+  smallAns
        else:
            currAns = 1+ dp[newcheckvalue]
        ans = min(ans, currAns)
    return ans

n = int(input())
dp = [-1 for i in range(n+1)]
ans = minSqueres(n, dp)
print(ans)