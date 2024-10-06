def has_duplicate(arr):
    return len(arr) != len(set(arr))

print(has_duplicate([1, 2, 3, 1]))
print(has_duplicate([1, 2, 3, 4]))

#=================================================


def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return False

arr = [5, 8, 3, 9, 12, 15]
num = 8
ket_qua = linear_search(arr, num)

print(f"số {num} được tìm thấy ở vị trí {ket_qua}")

def binary_search(arr, num):
    pass


#==================================================

def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    
    while left <= right:
        if arr[mid] == num:
            return mid
        elif arr[mid] > num:
            right = mid - 1
            mid = (left + right) // 2
        else:
            left = mid + 1
            mid = (left + right) // 2
            
    return False

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = 0
result = binary_search(arr, num)

if result != -1:
    print(f"Phần tử tìm thấy ở vị trí {result}")
else:
    print("phần tử trốn rồi")
