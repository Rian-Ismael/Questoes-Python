def convert_to_int(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])


def is_odd(arr):
    odd_array = []
    odd_count = 0

    for i in range(len(arr) - 1):
        if arr[i] % arr[i + 1] == 0:
            odd_array.append(arr[i])
            odd_array.append(arr[i + 1])
            odd_count += 1
    
        elif arr[i + 1] % arr[i] == 0:
            odd_array.append(arr[i])
            odd_array.append(arr[i + 1])
            odd_count += 1
    
    return odd_array, odd_count


def main():
    
    vals_array = input().split(' ')
    convert_to_int(vals_array)
    odds, odd_counter = is_odd(vals_array)

    print(f'{odd_counter} par(es)')

    for i in range(0, len(odds), 2):
        print(odds[i], odds[i + 1])

main()
