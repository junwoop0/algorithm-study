# Problem: 1926. Nearest Exit from Entrance in Maze
# Time: O(m*n) where m and n are the dimensions of the maze
# Space: O(m*n) for the queue and visited set in the worst case
# URL: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        visited = set()
        x0, y0 = entrance
        queue.append((x0,y0,0))
        visited.add((x0,y0))
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        while queue:
            r, c, step = queue.popleft()
            for x, y in directions:
                a = r+ x
                b = c + y
                u = step + 1
                if ((a,b) not in visited) and (0 <= a < len(maze) and 0 <= b < len(maze[0])) and (maze[a][b] == "."):
                    queue.append((a,b,u))
                    visited.add((a,b))
                    if a == 0 or b == 0 or a == len(maze)-1 or b == len(maze[0])-1:
                        return u
        return -1

'''
Notes
- Since you can't see the near neighbors using row, you have to make a list of directions to check for neighbors
- You can add tuple as elements in the queue
'''