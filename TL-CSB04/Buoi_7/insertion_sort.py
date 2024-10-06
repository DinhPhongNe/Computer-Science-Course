#---------====== Cách 1 ======-----------
# def insertion_sort(arr):
#   for i in range(1, len(arr)):
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and key < arr[j]:
#       arr[j + 1] = arr[j]
#       j -= 1
#     arr[j + 1] = key

#---------====== Cách 2 ======-----------
def insertion_sort(arr):
    arr_sorted = []
    while len(arr) != 0:
        # Cách 1
        max = 0
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
        arr_sorted.append(max)
        arr.remove(max)

        # Cách 2
        #m = min(arr)
        #arr_sorted.append(m)
        #arr.remove(m)
    return arr_sorted

artists = ["BLACKPINK", "N'SYNC", "The Beatles", "Mariah Carey", "Bruno Mars"]
plays = [141, 58, 20, 5, 102]

data = list(zip(artists, plays))

sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

for artist, play in sorted_data:
    print(f"{artist}: {play}")