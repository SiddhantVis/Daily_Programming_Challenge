def duplicatevalues(arr, n):
    for a in range(n):
        for b in range(a + 1, n):
            if (arr[a] == arr[b]):
                return arr[a]


if __name__ == "__main__":
    arr = [1,3,5,6,2,4,2]
    n = len(arr)

    print(duplicatevalues(arr, n))