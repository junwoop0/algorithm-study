# Problem: 1448. Count Good Nodes in Binary Tree
# Time: O(n)
# Space: O(h) where h is the height of the tree
# URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def recursive(root, val):
            nonlocal count
            if root is None:
                return
            if root.val >= val:
                val = root.val
                count += 1
            recursive(root.left, val)
            recursive(root.right, val)
            return count
        recursive(root, root.val)
        return count
    
'''
Notes
- Use nonlocal variable to store the count of good nodes
- Remember that you have to return something in the recursive function, otherwise it will return None by default
'''