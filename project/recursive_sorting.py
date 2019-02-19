### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : int(len( arr ) / 2) ] )
        right = merge_sort( arr[ int(len( arr ) / 2) : ] )
        print(left,right)
        arr = merge( left, right )   # merge() defined later
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
#arr2 = []
#arr3 = [0, 1, 2, 3, 4, 5]

#print(merge_sort(arr1))
#print(merge_sort(arr2))
#print(merge_sort(arr3))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION


def quick_sort( arr, high, low ):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    under = []
    over = []
    for i in range(1,len(arr)):
        if arr[i] > pivot:
            over.append(arr[i])
        else:
            under.append(arr[i])

    return [*quick_sort(under,None,None), pivot, *quick_sort(over,None,None)]

#print(quick_sort(arr1,0,0) )

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
