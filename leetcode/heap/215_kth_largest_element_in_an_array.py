# Problem: 215. Kth Largest Element in an Array
# Time: O(n + k log n) where n is the length of the input array and k is the given integer.
# Space: O(n)
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        for i in range(k):
            ans = heapq.heappop(max_heap)
        return -ans

'''
Notes
- Since heap gives us the smallest element, we can get the biggest element by multiplying the elements by -1
'''
