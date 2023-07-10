from stack_function import stack

s = stack()

s.push(13)
s.push(12)
s.push(14)
s.push(18)

while s.isEmpty() is False:
    print(s.pop())
s.top()