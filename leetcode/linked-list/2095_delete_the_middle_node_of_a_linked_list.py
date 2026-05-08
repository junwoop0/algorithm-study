# Problem: 2095. Delete the Middle Node of a Linked List
# Time: O(n)
# Space: O(1)
# URL: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        if head.next == None:
            return None
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head

'''
Notes
- You can use two pointers to find the middle node. One pointer is a slower one and the other pointer is a faster one.
- Think of the case when prev is None. It means that the list has only one node.
'''