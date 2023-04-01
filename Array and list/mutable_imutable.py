# immutable variables

# a = 3
# x = 3
# print(a, x)
# x = 4

# print(a,x)

# mutable list

# a = [1, 3, 4 ,5]
# x = a
# print(a,x)

# x[1]=4
# print(a, x)

# x = [33,7,8]

# print(x, a)

# def sum(a):
#     a = a+2
#     return a
# a = 2
# sum(2)
# print(a)
# def sum(a):
#     a = a+2
#     return a
# a = 2
# a = sum(2)
# print(a)

# def multiplication(x,a):
#     a = a*x
#     return a

# a = 5
# x= 6

# result = multiplication(x, a)
# print(result)


# passing list through the function

def passingThroughList(li):
    # li[0] = li[0]+2
    li = [5,6,7]
    return li

li = [1,2,3,4]
li = passingThroughList(li)
print(li)