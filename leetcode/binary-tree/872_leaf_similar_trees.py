# Problem: 872. Leaf-Similar Trees
# Time:
# Space: 
# URL: https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first = []
        second = []
        def recursive(root, arr):
            if root is None:
                return
            if (root.left == None) and (root.right == None):
                arr.append(root.val)
            recursive(root.left, arr)
            recursive(root.right, arr)
        recursive(root1, first)
        recursive(root2, second)
        return first == second

'''
Notes
- You have to append the value of the leaf node to the list, not the node itself
'''
