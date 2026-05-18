# Problem: 841. Keys and Rooms
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = deque()
        stack.append(0)
        visited = set()
        visited.add(0)
        while stack:
            node = stack.popleft()
            for next_node in rooms[node]:
                if next_node not in visited:
                    stack.append(next_node)
                    visited.add(next_node)
        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True

'''
Notes
- You can delete a row by using pop()
- You can add an element in the set by using add()
'''