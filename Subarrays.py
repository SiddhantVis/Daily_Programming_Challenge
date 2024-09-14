def find_subarrays_with_zero_sum(arr):

    n = len(arr)
    prefix_sum = [0] * (n + 1)
    prefix_sum_map = {}
    result = []

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

        if prefix_sum[i] in prefix_sum_map:
            start_index = prefix_sum_map[prefix_sum[i]]
            end_index = i - 1
            result.append((start_index, end_index))
        else:
            prefix_sum_map[prefix_sum[i]] = i

    return result

# Example usage:
arr = [1, 2, -3, 3, -1, 2]
subarrays = find_subarrays_with_zero_sum(arr)
print(subarrays)