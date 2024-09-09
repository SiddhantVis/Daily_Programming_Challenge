def arrange(arr, n):
    low = 0
    high = n - 1
    mid = 0

    while mid <= high:

      if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low = low + 1
        mid = mid + 1

      elif arr[mid] == 1:
        mid = mid + 1

      else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high = high - 1
    return arr

def displayArray(arr):
    for k in arr:
        print(k, end=' ')

arr = [0,0,2,0,1,2,1,2]
n = len(arr)
arr = arrange(arr, n)
displayArray(arr)