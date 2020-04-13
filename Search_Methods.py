# Sam Cole
# 4/13/2020
# These are the search methods


# This is bubble sort
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr


# this is the selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j
        # Place it at the front of the sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


# This is the insertion sort
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
    return arr


# this is the merge sort
def merge_lists(left_sublist,right_sublist):
    i,j = 0,0
    result = []
    # iterate through both left and right sublist
    while i < len(left_sublist) and j < len(right_sublist):
        # if left value is lower than right then append it to the result
        if left_sublist[i] <= right_sublist[j]:
            result.append(left_sublist[i])
            i += 1
        else:
            # if right value is lower than left then append it to the result
            result.append(right_sublist[j])
            j += 1
    # concatenate the rest of the left and right sublists
    result += left_sublist[i:]
    result += right_sublist[j:]
    # return the result
    return result


def merge_sort(input_list):
    # if list contains only 1 element return it
    if len(input_list) <= 1:
        return input_list
    else:
        # split the lists into two sublists and recursively split sublists
        midpoint = int(len(input_list)/2)
        left_sublist = merge_sort(input_list[:midpoint])
        right_sublist = merge_sort(input_list[midpoint:])
        # return the merged list using the merge_list function above
        return merge_lists(left_sublist,right_sublist)


# This is quick sort
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx


def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)
    return array


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    return quick_sort_recursion(array, begin, end)
