def shifted_arr_search(shiftArr, num):
    left, right = 0, len(shiftArr) - 1
    while left < right:
        mid = (right - left) // 2
        if shiftArr[left] <