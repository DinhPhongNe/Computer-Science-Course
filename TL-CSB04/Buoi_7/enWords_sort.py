def bubble_sort(words_arr):
    arr = words_arr.split()
    
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if len(arr[j]) > len(arr[j + 1]) or (len(arr[j]) == len(arr[j + 1])):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    sorted_words = " ".join(arr)
    return sorted_words

most_common_100 = "the of to and a in is it you that he was for on are with as I his they be at one have this from or had by hot but some what there we can out other were all your when up use word how said an each she which do their time if will way about many then them would write like so these her long make thing see him two has look more day could go come did my sound no most number who over know water than call first people may down side been now find"


print(bubble_sort(most_common_100))

print()