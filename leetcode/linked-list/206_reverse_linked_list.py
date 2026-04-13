# Problem: 206. Reverse Linked List
# Time: O(n)
# Space: O(1)
# URL: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prev = None
        while True:
            current = head.next
            head.next = prev
            prev = head
            if current == None:
                break
            head = current
        
        return head
    
'''
Notes
- Always think of the case with empty list
'''
