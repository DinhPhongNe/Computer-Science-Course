def double_pivot_compression_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid_index = len(arr) // 2
    mid_pivot = arr[mid_index]
    end_pivot = arr[-1]
    
    low_part = []
    middle_part = []
    high_part = []
    
    for num in arr[:-1]:
        if num < mid_pivot:
            low_part.append(num)
        elif num > end_pivot:
            high_part.append(num)
        else:
            middle_part.append(num)
    
    sorted_low = double_pivot_compression_sort(low_part)
    sorted_middle = double_pivot_compression_sort(middle_part)
    sorted_high = double_pivot_compression_sort(high_part)
    
    return sorted_low + [mid_pivot] + sorted_middle + [end_pivot] + sorted_high

arr = [5, 2, 9, 1, 5, 6, 7, 3, 4]
sorted_arr = double_pivot_compression_sort(arr)
print("Danh sách đã sắp xếp:", sorted_arr)
