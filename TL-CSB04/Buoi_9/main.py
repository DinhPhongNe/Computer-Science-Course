def gop_hai_mang(nums1, nums2):
    gop_mang = [0] * (len(nums1) + len(nums2))
    i = 0
    j = 0
    k = 0

    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            gop_mang[k] = nums1[i]
            i += 1
        else:
            gop_mang[k] = nums2[j]
            j += 1
        k += 1

    while i < len(nums1):
        gop_mang[k] = nums1[i]
        i += 1
        k += 1

    while j < len(nums2):
        gop_mang[k] = nums2[j]
        j += 1
        k += 1

    return gop_mang

nums1 = [1, 2, 3]
nums2 = [2, 5, 6]

result = gop_hai_mang(nums1, nums2)
print(result)
print("Do phuc tap la: O(n+m) voi n la do dai nums1 va m la do dai nums2 ")
print("💯👌")
