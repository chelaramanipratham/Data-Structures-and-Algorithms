def lastOccurence(arr, n, x):
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) >> 1

        if arr[mid] < x: low = mid + 1
        if arr[mid] > x: high = mid - 1
        else:
            if mid == n-1 or arr[mid] != arr[mid + 1]:
                return mid
            else: low = mid + 1

    return -1

print(lastOccurence([5, 10, 10, 10, 20], 5, 10))