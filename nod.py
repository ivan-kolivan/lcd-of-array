def nod(arr, index=0):
    while arr[index] != arr[index + 1]:
        if arr[index] > arr[index + 1]:
            arr[index] -= arr[index + 1]
        else:
            arr[index + 1] -= arr[index]
    if index + 1 == len(arr) - 1: return arr[index]
    return nod(arr, index+1)