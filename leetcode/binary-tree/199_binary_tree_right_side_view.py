# Problem: 199. Binary Tree Right Side View
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = list()
        queue = deque()
        if root is not None:
            queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            ans.append(node.val)
            
        return ans

'''
Notes
- You can get to deeper level after you pop the amount of nodes in the current level
'''