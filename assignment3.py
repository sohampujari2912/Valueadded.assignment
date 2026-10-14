# Q3-Check if the Array is Sorted 
def isArraySorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True
