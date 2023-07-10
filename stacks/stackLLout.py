from stackLL import stack


s = stack()
s.push(12)
s.push(23)
s.push(45)
s.push(5)

while s.isEmpty() is False:
    print(s.pop())
print(s.top())