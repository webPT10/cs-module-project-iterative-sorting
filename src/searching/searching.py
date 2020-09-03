def linear_search(arr, target):
    # Your code here
    for q in range(len(arr)):
        if arr[q] == target:
            return q

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    middle = 0

    while low <= high:
        middle = (high + low) // 2

        # check if TARGET is present at MIDDLE
        if arr[middle] < target:
            low = middle + 1

        # if TARGET is Greater, ignore Left half
        elif arr[middle] > target:
            high = middle - 1

        # if TARGET is Smaller, ignore Right half
        else:
            return middle

    return -1  # not found
