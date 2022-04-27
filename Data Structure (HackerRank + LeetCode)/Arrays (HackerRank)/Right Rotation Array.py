
def rotateRight(arr, d):
    new_arr = [0] * len(arr)
    for i in range(len(arr)):
        # val = arr[i]
        new_arr[(i + d) % len(arr)] = arr[i]
        # print(arr)
    # print(new_arr)
    return new_arr


