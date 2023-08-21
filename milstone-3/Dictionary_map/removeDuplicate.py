def removeDuplicate(s):
    ans = ''
    d = {}
    for i in s:
        if i not in d:
            ans = ans+i
            d[i] = True
    return ans

s=input() 
print(removeDuplicate(s))