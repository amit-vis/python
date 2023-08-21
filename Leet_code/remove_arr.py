# def removeElement(nums, val):
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k]=nums[i]
#             k+=1
#     return k

def removeDuplicate(nums):
    k =0
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[k] = nums[i]
            k+=1
    return k
        

nums = [int(x) for x in input().split()]

result = removeDuplicate(nums)
print(result)