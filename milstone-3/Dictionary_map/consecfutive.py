def consecutive(arr):
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = True

    max_start_point = 0
    max_length = 0
    for i in range(len(arr)):
        temp_start = arr[i]
        temp_length = 1
        while d.get(temp_start+temp_length) is not None:
            temp_length += 1
        if temp_length>max_length:
            max_length = temp_length
            max_start_point = temp_start
    return max_start_point, max_start_point+max_length-1

arr = [int(x) for x in input().split()]
print(consecutive(arr))
