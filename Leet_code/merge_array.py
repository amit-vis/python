def merge(nums1, n, nums2, m):
    p1 = n-1
    p2 = m-1
    p=m+n-1
    while p1>=0 and p2>=0:
        if nums1[p1]>nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    nums1[:p2+1] = nums2[:p2+1]
    return nums1


nums1 = [int(x) for x in input().split()]
n= int(input("Enter the number n: "))
nums2 = [int(y) for y in input().split()]
m = int(input("Enter the number of m: "))

result = merge(nums1, n, nums2, m)
print(result)

