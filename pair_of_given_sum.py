"""
Task:
Given an array of n integers and a target value, the task is to find whether there is a pair of elements in the array whose sum is equal to target.

Sample Input 1:
arr = [0, -1, 2, -3, 1]
target = -2

Sample Output 1:
True

Sample Input 2:
arr = [1, -2, 1, 0, 5]
target = 0

Sample Output 2:
False

Explanation:
If we calculate the sum of the output, 1 + (-3) = -2
"""

def pair_sum(arr, target):
    seen = []
    for num in arr:
        complement = target - num
        if complement in seen:
            return True  # Pair found
        seen.append(num)  # Add the current number to the list
    return False  # No pair found

arr = list(map(int, input().split()))
target = int(input())

print(pair_sum(arr, target))