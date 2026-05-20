# Problem: 547. Number of Provinces
# Time: O(n^2)
# Space: O(n)
# URL: https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        stack = deque()
        visited = set()
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                stack.append(i)
                visited.add(i)
                while stack:
                    city = stack.pop()
                    for i in range(len(isConnected)):
                        if isConnected[city][i] == 1 and i not in visited:
                            visited.add(i)
                            stack.append(i)
                count += 1
        return count

'''
Notes
- You have to set index to mark visited, not the value of the element in the matrix
- It's better to use different variable for two different loops for readability
'''
