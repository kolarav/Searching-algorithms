import math
from typing import List


#  Time : O(N^0.5) as the jump size here is sqrt of N. 
def jump_search(nums: List[int],target: int) -> bool:
    '''
        In jump search we start from 0th index and compare if the target is found or not,
        if found the return True or we increase the upper index bound by 2^N where N is the 
        no of element in the list. Now We check if lower elementis lesser than target and 
        upper element is greater than taget  or not and accordingly increase or decrese
        lower and upper bound.   '''
        
    previous = 0
    current = math.sqrt(len(nums))
    while(current < len(nums)):
        if(nums[int(previous)] <= target and nums[int(current)] >= target):
            while(previous < current):
                if(nums[int(previous)] == target):
                    return True
                else:
                    previous += 1
        else:
            previous = current
            current += math.sqrt(len(nums))
    return False


numbers = [1, 3, 5, 10, 15, 21, 23, 25, 30, 58, 67, 77,
        79, 83, 89, 95, 110, 134, 153, 165, 172, 189, 200]
print(jump_search(numbers, 154))
