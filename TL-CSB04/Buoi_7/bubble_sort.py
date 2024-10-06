def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

music_data = [
    ["BLACKPINK", 141],
    ["N'SYNC", 58],
    ["The Beatles", 20],
    ["Mariah Carey", 5],
    ["Bruno Mars", 102]
]

sorted_music_data = bubble_sort(music_data)

print("Danh sách ca sĩ yêu thích (theo số lượt nghe giảm dần):")
for artist, plays in sorted_music_data:
    print(f"{artist}: {plays} lượt nghe")
