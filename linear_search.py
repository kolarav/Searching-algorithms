from typing import List


# Time : O(N) as we are going through all the elements.
def linear_search(nums: List[int], target: int) -> int :
    for idx in range(len(nums)):
        if(nums[idx] == target):
            return idx
        return -1


numbers = [1, 3, 5, 10, 15, 21, 23, 25, 30, 58, 67, 77,
        79, 83, 89, 95, 110, 134, 153, 165, 172, 189, 200]
print(linear_search(numbers, 154))
