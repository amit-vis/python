# def tripletSum(arr,X):
#     arr.sort()
#     l = []
#     for i in range(0,len(arr)-2):
#         sum = X - arr[i]

#         start = i+1
#         end = len(arr)-1
#         while start <end:
#             t = arr[start]+arr[end]
#             if sum == t:
#                 l.append([arr[start],arr[i],arr[end]])
#                 start +=1
#                 end -=1
#             elif t<sum:
#                 start +=1
#             else:
#                 end -=1
#     return len(l)

# another approach of triplet sum
def triplet(arr,X):
    start = 0
    end = len(arr)-1
    l = []
    while start<end:
        sum_s = arr[start]+arr[end]
        if X == sum_s:
            l.append([arr[start],arr[end]])
            start +=1
            end -=1
        elif X<sum_s:
            start +=1
        else:
            end -=1
    return l

arr = [int(x) for x in input().split()]
X = int(input())
print(triplet(arr,X))