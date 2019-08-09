# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # iterate through the entire array
    for i in range(0, len(arr)):
        # for each index of the array iterate through the rest of the array
        for j in range(0, len(arr)-1):
            # compare elements next to each other
            # if they are out of order
            if arr[j] > arr[j+1]:
                # swap them
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    if arr == []:
        return arr
    if min(arr) < 0:
        return 'Error, negative numbers not allowed in Count Sort'

    # container objects
    spread = range(min(arr), max(arr)+1)
    count = {}
    # count = {key: 0 for key in range(min(arr), max(arr))}
    # get our occurances
    for i in arr:
        occurs = count.get(i, 0) + 1
        count[i] = occurs

    # build out our positions
    sum = 0
    for key in spread:
        # get the key and if its not present get 0
        occurs = count.get(key, 0)
        sum += occurs
        count[key] = sum

    # reassemble
    sorted = []
    total = 0
    for key in spread:
        while count[key] - total > 0:
            sorted.append(key)
            total += 1

    return sorted


""" 
    I accidentally pushed to master so this comment is gonna let me make my PR
"""
