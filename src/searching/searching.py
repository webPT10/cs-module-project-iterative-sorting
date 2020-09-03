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

    # #set two different pointers, low & high
    # low = 0 # first item
    # high = len(arr) - 1 # last item

    # # Your code here
    # while low <= high: # loop while low pointer LESS/EQUAL to high point
    #     # middle index, variable middle
    #     middle = (low + high) // 2 # average low & high divide by 2
    #     the_guess = arr[middle] # middle index used to retrieve item w/ that index from List
        
    #     # set up logic using IF statements
    #     if the_guess == target:
    #         return middle

    #     if the_guess > target:
    #         high = middle - 1 # change HIGH pointer to index directly below current MIDDLE value
        
    #     else:
    #         low = middle + 1 # change LOW pointer to be equal to index directly after current MIDDLE value

        # if reaching here, Element not present
    return -1  # not found
