def checkRedundant(exp):
    s = []
    for char in exp:
        if char == ")":
            top = s.pop()
            isRedundant = True
            while top != "(":
                if top in "+-*/":
                    isRedundant = False
                top = s.pop()
            if isRedundant:
                return True
        else:
            s.append(char)
    if not s:
        return s
    else:
        return -1

exp = input()
result= checkRedundant(exp)
print(result)