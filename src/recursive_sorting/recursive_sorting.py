# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    merged_arr = []

    while len(arrA) > 0 and len(arrB) > 0:
        lowest = arrA.pop(0) if arrA[0] < arrB[0] else arrB.pop(0)
        merged_arr.append(lowest)

    merged_arr += arrA + arrB

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):

    # a
    # 3, 5, 6, 8, 1, 2, 7, 9
    #             b

    # Get the start and end points so we can increment them as we go
    a = start
    b = mid

    # While we still have leftover items in each half
    # this loop logic was an issue
    while a < b and b < end:
        # if item a > item b we need to bring b to the beginning of the array
        if arr[a] > arr[b]:
            c_index = b
            # lets keep flipping these guys until we get it at the beginning of the array
            while c_index > a:
                arr[c_index], arr[c_index-1] = arr[c_index-1], arr[c_index]
                c_index -= 1
            b += 1

        # everytime we put a piece of the array in order a needs to increment
        a += 1

    return arr


def merge_sort_in_place(arr, l, r):
    """ l and r refer to the left and right bounds of the section of arr we are looking at """

    # if we only have 1 element left
    if r-l <= 1:
        return arr

    # get the middle index of the section we're looking at
    mid = (r - l) // 2 + l

    # do the left side
    merge_sort_in_place(arr, l, mid)
    # do the right side
    merge_sort_in_place(arr, mid, r)

    # return and merge the 2 now sorted sides
    return merge_in_place(arr, l, mid, r)


print(merge_in_place([2, 4, 5, 6, 1, 3, 5, 9], 0, 4, 8))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
