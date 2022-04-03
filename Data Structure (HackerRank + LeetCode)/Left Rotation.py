def rotateLeft(d, arr):
    # Write your code here
    new_arr = [0] * len(arr)
    for i in range(len(arr)):
        val = arr[i]
        new_arr[i-d] = val
        # print(arr)
    return new_arr