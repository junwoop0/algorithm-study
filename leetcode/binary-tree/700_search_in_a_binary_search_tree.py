# Problem: 700. Search in a Binary Search Tree
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recursive(root, val):
            if root is None:
                return
            if root.val == val:
                return root
            left = recursive(root.left, val)
            if left is not None:
                return left
            right = recursive(root.right, val)
            if right is not None:
                return right
        return recursive(root, val)