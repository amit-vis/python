a = {"the":3, "a": 4, 100: "Amit"}
# print(type(a))
# print(a)

b = a.copy()
# print(b)
# print(len(b))

c = dict([("the", 2), ("a", 4), (1000, "ghjedgf")])

# print(c)

d = dict.fromkeys(["the", "a", 56], [120, 3456,786])
# print(d)


# Access data

e = {1:2, 3:4, 'list': [1,45], 'dict': {5:6}}

# print(e)
# print(e['list'])

# print(e.get('di'))

# print(e.get('li', 0))

# print(e.keys())
# print(e.values())
# print(e.items())

# for i in e:
#     print(i, e[i])

# for i in e.values():
#     print(i)

# print("list" in e)

e["tuple"] = (3,5,6)

# print(e)

f = {3:7, 'the':8, 2:1000}

e.update(f)
print(e)

e.pop('tuple')
print(e)

del e[1]

print(e)

e.clear()
print(e)

del e
print(e)