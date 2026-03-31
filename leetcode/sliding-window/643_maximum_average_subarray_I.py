# Problem: 643. Maximum Average Subarray I
# Time: O(n)
# Space: O(1)
# URL: https://leetcode.com/problems/maximum-average-subarray-i/


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        slot = sum(nums[0:k]) / k
        best = slot
        length = len(nums)
        for i in range(0, length - k):
            slot -= nums[i] / k
            slot += nums[i + k] / k
            if slot > best:
                best = slot
        return best
    
'''
Notes
- Always think of edge cases, like when k is 1, or when k is equal to the length of the array
- You can use sum() function to calculate the sum of the first k elements in the array
- Instead of comparing slot and best with if statement, you can use max() function to update best
- Instead of dividing each element by k, you can divide the final sum by k in the final return statement
'''