from typing import List

#  In case of binary search the sequence is always sorted so first we check
#  if the target value is in the range or not, that is if it is in between 
#  the range of first and last elemnt of the list. If not we return -1 else 
#  we first find the mid point of the list and check if it is equals to the
#  target if it is then we return mid point else we check if the mid point 
#  value is higher or lower than the target value and search the lower or 
#  upper sub list accordingly.


# Time: O(log(N)) as in every iteration we are dividing the list in to half and searching again.

# Recursive method
def binary_search(nums: List[int] , target: int) -> int:
  
    if(target<nums[0] or target>nums[-1]):
        return -1
    if(nums[0] == target):
        return 0 
    if(nums[-1] == target):
        return len(nums)-1
    mid = (len(nums)-1)//2
    if(nums[mid] == target):
        return mid
    elif(len(nums)>1):
        if(nums[mid] > target):
            return (binary_search(nums[0:mid], target))
        else:
            return (mid + 1 + binary_search(nums[mid+1:], target))   
    return False

numbers = [1, 3, 5, 10, 15, 21, 23, 25, 30, 58, 67, 77,
        79, 83, 89, 95, 110, 134, 153, 165, 172, 189, 200]
print(binary_search(numbers, 67))





# Iterative Method
# def binary_search(nums: List[int] , target: int) -> int:
#     lower = 0
#     upper = len(nums)-1
#     while(upper >= lower):
#         mid = (lower + upper)//2
#         if(nums[mid]==target):
#             return mid
#         else:
#             if(nums[mid] > target):
#                 upper = mid - 1
#             else:
#                 lower = mid + 1
#     return (-1)


