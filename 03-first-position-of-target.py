# encoding=utf-8

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(nums, target):
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

# A = [1,4,4,5,7,7,8,9,9,10]#，1

A = [1, 2, 3, 3, 4, 5, 10]#，3

# A = [1, 2, 3, 3, 4, 5, 10]#，6   
print("The answer is: "+ str(Solution.binarySearch(nums=A, target=3)))  




