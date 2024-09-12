def merge_values(a, b, m, n):

    for i in range(n-1, -1, -1):

        last = a[m-1]
        j = m-2
        while(j >= 0 and a[j] > b[i]):
            a[j+1] = a[j]
            j -= 1

        if (last > b[i]):

            a[j+1] = b[i]
            b[i] = last

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
m = len(a)
n = len(b)

merge_values(a, b, m, n)

print("After Merging \nFirst Array:", end="")
for i in range(m):
    print(a[i], " ", end="")

print("\nSecond Array: ", end="")
for i in range(n):
    print(b[i], " ", end="")
