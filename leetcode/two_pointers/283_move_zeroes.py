# Problem: 283. Move Zeroes
# Time: O(n^2)
# Space: O(1)
# URL: https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] == 0:
                for i in range(start, end):
                    nums[i] = nums[i+1]
                nums[end] = 0
                end -= 1
            if nums[start] != 0:
                start += 1
                
'''
Notes
- You have to think of a case when zero is in a row
- You can reduce the time complexity by using two pointers, one for the current position and another for the next non-zero element.
'''