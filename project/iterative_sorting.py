# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    i = 1
    while i < len(arr):
        if i == 0:
            i = 1
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
        else:
            i += 1
    return arr

# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = True
    while swap:
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True



    return arr

# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# arr2 = []
# arr3 = [0, 1, 2, 3, 4, 5]

# print(bubble_sort(arr1))
# print(bubble_sort(arr2))
# print(bubble_sort(arr3))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr