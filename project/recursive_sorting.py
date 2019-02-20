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
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        right = merge_sort( arr[ len( arr ) // 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):

    def median_of_3(arr, low, high):
        mid = (low + high) // 2
        if arr[low] >= arr[mid] and arr[low] <= arr[high]:
            return low
        elif arr[low] <= arr[mid] and arr[low] >= arr[high]:
            return low
        elif arr[mid] >= arr[low] and arr[mid] <= arr[high]:
            return mid
        elif arr[mid] <= arr[low] and arr[mid] >= arr[high]:
            return mid
        else:
            return high
    
    def partition(arr, low, high):
        # Set up the pivot
        pivot_index = median_of_3(arr, low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], pivot

        # Work two indeces inward from the outside to the middle, switching their values when they are both on the wrong
        # sides of the pivot, and stopping when they meet in the middle
        i, j = low, high - 1
        while j > i:
            
            # If both values are already on the correct side of the partition, move them inwards (unless they would pass each
            # other, then just move the left one)
            if arr[j] >= pivot and arr[i] <= pivot:
                i += 1
                if (j > i):
                    j -= 1
            # Otherwise, if they're both on the wrong side of the partition, swap them
            elif arr[j] < pivot and arr[i] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
            # Otherwise, move the one of the two indeces that's not ready to swap
            elif arr[i] <= pivot:
                i += 1
            else:
                j -= 1

        # If any values were greater than pivot, put the pivot value in the position where the two moving indeces met
        if j < high - 1 or arr[j] > arr[high]:
            arr[i], arr[high] = arr[high], arr[i]

        # Return where the pivot is
        return i

    # Non-Base Case, Recursive Invocation:
    if high > low:      # If there are at least two elements to be sorted
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
