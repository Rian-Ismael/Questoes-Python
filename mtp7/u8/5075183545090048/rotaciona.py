def rotdir(array):
    for i in range(len(array)):
        array[len(array)-1], array[i] = array[i], array[len(array)-1]
    return array
