def idosos_inicio(array):
    start = 0
    for i in range(len(array)):
        for j in range(start, len(array)):
            if array[i] >= 60:
                if array[i] > array[j]:
                    array[j], array[i] = array[i], array[j]
                    start += 1

    return array


array = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
print(idosos_inicio(array))
assert idosos_inicio(array) == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]
