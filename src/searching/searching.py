def linear_search(arr, target):
    # Your code here
    for n in range(len(arr)):
        if arr[n] == target:
            return n

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    min = 0
    max = (len(arr)-1)
    while min <= max:
        mid = min + (max -1)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            min = mid + 1
        else:
            max = mid - 1

    return -1  # not found
