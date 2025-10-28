# optimal O(n) solution
def two_sum(num_list, target):

    length = len(num_list)

    found_nums = {}

    for i in range(length):
        second_value = target - num_list[i]

        if second_value in found_nums:
            return [found_nums[second_value], i]
        
        found_nums[num_list[i]] = i
        
    return []

print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )