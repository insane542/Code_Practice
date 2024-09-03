"""
Find substring with a given sum in a given integer array. Find subsarrays with given sum in it.
Eg: arr = [3, 4, -7, 1, 3, 3, 1, -4]
target = 7
"""

def subarray_is_target(array, target):
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            if current_sum == target:
                print(array[i:j+1])

inp = [3, 4, -7, 1, 3, 3, 1, -4]
target = 7
subarray_is_target(inp, target)