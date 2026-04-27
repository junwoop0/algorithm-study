# Problem: 238. Product of Array Except Self
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        left_val = 1
        right = [1]
        right_val = 1
        ans = []
        for x in nums[:-1]:
            left_val *= x
            left.append(left_val)
        for x in reversed(nums[1:]):
            right_val *= x
            right.append(right_val)
        for i in range(len(nums)):
            ans.append(left[i]*right[len(nums)-i-1])
        return ans
    
'''
Notes
- We can solve this problem without division by calculating the product of all the elements twice, 
once from the left and once from the right.
- Also, you don't need to make ans list, you can just calculate the product and store it in the left list.
'''