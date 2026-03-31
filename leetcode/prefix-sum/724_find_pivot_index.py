# Problem: 724. Find Pivot Index
# Time: O(n)
# Space: O(1)
# URL: https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        pivot = 0
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return pivot
            left += nums[i]
            pivot += 1
        return -1
    
'''
Notes
- You don't need to use pivot variable. You can just return i instead of pivot.
'''
