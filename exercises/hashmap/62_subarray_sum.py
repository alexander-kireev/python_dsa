def subarray_sum(nums, target):
    seen_sums = {0: -1}   
    current_sum = 0

    length = len(nums)

    for i in range(length):
        current_sum += nums[i]

        if (current_sum - target) in seen_sums:
            return [(seen_sums[current_sum - target] + 1), i]

        seen_sums[current_sum] = i

    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""