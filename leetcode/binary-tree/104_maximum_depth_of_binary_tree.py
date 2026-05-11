# Problem: 104. Maximum Depth of Binary Tree
# Time: O(n)
# Space: O(h) where h is the height of the tree
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        count = 0
        def recursive(root):
            nonlocal count
            nonlocal depth
            count += 1
            if root is None:
                count -= 1
                depth = max(depth, count)
                return
            recursive(root.left)
            recursive(root.right)
            count -= 1 # You need to subtract 1 when you climb up the tree, because you are going back to the parent node
        recursive(root)
        return depth
    

'''
Notes
- Use nonlocal variable to store the maximum depth
- You need to subtract 1 when you climb up the tree, because you are going back to the parent node
'''