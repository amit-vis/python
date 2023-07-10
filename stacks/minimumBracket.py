def minimuBracket(string):
    # if len(string)%2 != 0:
    #     return -1
    # stack = []
    # for char in string:
    #     if char == "{":
    #         stack.append(char)
    #     elif char == "}":
    #         if stack and stack[-1] == "{":
    #             stack.pop()
    #         else:
    #             stack.append(char)
    # open_bracket = 0
    # close_bracket = 0
    # for char in stack:
    #     if char == "{":
    #         open_bracket +=1
    #     else:
    #         close_bracket += 1
    # return (open_bracket//2)+(close_bracket//2)

    # another approach
    if len(string)%2 != 0:
        return -1
    if len(string) == 0:
        return 0
    s = []
    for char in string:
        if char == "{":
            s.append(char)
        else:
            if s and s[-1] == "{":
                s.pop()
            else:
                s.append(char)

    count = 0
    while len(s) >=2:
        c1 = s.pop()
        c2 = s.pop()
        if c1 != c2:
            count += 2
        else:
            count += 1
    return count

s = input()
result = minimuBracket(s)
print(result)