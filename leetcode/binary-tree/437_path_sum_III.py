# Problem: 437. Path Sum III
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path = {0:1}
        count = 0
        currSum = 0
        def recursive(root, currSum):
            nonlocal count
            if root is None:
                return
            currSum += root.val
            count += path.get(currSum - targetSum, 0)
            path[currSum] = path.get(currSum, 0) + 1
            left = recursive(root.left, currSum)
            right = recursive(root.right, currSum)
            path[currSum] -= 1
        recursive(root, currSum)
        return count
    
    
'''
Notes
- You have to set key as the sum of the path and value as the number of paths that have that sum
- The initial dictionary should have key 0 and value 1 because there is one path that has sum 0, which is the empty path
- You have to count first and then update the dictionary
'''