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
    count = {}
    for i in len(arr):
        pass

    return arr


""" 
    I accidentally pushed to master so this comment is gonna let me make my PR
"""
