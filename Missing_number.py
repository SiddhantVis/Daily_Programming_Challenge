def number_missing(num, arr):
    sum_arr = sum(arr)

    expected_sum = (num * (num + 1)) // 2
    return expected_sum - sum_arr


arr = [1,2,4,5]
num = 5
print(number_missing(num, arr))



