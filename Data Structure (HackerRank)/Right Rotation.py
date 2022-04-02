
def rotateRight(arr, d):
    new_arr = [0] * len(arr)
    for i in range(len(arr)):
        # val = arr[i]
        new_arr[(i + d) % len(arr)] = arr[i]
        # print(arr)
    # print(new_arr)
    return new_arr

if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1]
    assert rotateRight(a, 1) == [3, 1, 2]
    assert rotateRight(b, 1) == [1]