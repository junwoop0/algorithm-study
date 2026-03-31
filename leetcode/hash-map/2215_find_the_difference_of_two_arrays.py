# Problem: 2215. Find the Difference of Two Arrays
# Time: O(n + m)
# Space: O(n + m)
# URL: https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        remove_nums1 = set(nums1)
        remove_nums2 = set(nums2)
        nums1 = [x for x in set(nums1) if x not in remove_nums2]
        nums2 = [x for x in set(nums2) if x not in remove_nums1]
        return [nums1, nums2]

'''
Notes
- You can use set to make no duplicate values
- remember this expression, [x for x in set(nums1) if x not in set(nums2)]
'''
