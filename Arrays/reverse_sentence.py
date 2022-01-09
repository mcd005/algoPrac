def reverse_words(arr):
    arr.reverse()

    def reverse_subarray(start, end):
        nonlocal arr
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    word_start = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == ' ':
            reverse_subarray(word_start, i - 1)
            word_start = i + 1
    reverse_subarray(word_start, n - 1)

    return arr

print(reverse_words(["h","e","l","l", "o"]))