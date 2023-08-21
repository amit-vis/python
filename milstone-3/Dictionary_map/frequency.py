# s = "i have many many ball for a you ball"

# def frequency(s,k):
#     words = s.split()
#     d = {}
#     for w in words:
#         d[w] = d.get(w,0) + 1

#     for w in d:
#         if d[w]==k:
#             print(w)

# frequency(s,2)


# maximum frequency
def maxFrequency(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i,0)+1

    ans = arr[0]
    for i in arr:
        if d[i] > arr[ans]:
            ans = i
    return ans

arr = [2, 12, 2, 11, 12, 2, 1, 2, 2, 11, 12, 2, 6 ]
print(maxFrequency(arr))

