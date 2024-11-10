def intersection(nums1, nums2):
    result = []
    for num in nums1:
        if num in nums2 and num not in result:
            result.append(num)
    return result
    

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))

nums1 = [5, 7, 9]
nums2 = [5, 9, 3, 6]
print(intersection(nums1, nums2))