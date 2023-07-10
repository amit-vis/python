from stackLL import stack

def reverse(s1, s2):
    # if s1.isEmpty():
    #     return
    # temp = s1.pop()
    # reverse(s1,s2)
    # s2.push(temp)
    if len(s1)<=1:
        return
    while len(s1) !=1:
        ele=s1.pop()
        s2.append(ele)
    lastElement = s1.pop()
    while len(s2) !=0:
        ele = s2.pop()
        s1.append(ele)
    reverse(s1, s2)
    s1.append(lastElement)


s1 = [int(x) for x in input().split()]
s2 = []

reverse(s1, s2)

while len(s1) !=0:
    print(s1.pop(), end=" ")
    
    

    
