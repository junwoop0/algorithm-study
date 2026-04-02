# Problem: 933. Number of Recent Calls
# Time: O(n^2) in the worst case
# Space: O(n)
# URL: https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.data = []

    def ping(self, t: int) -> int:
        self.data.append(t)
        while self.data[0] not in range(t-3000, t+1):
            self.data.pop(0)
        return len(self.data)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

'''
Notes
- If I pop an element in the for loop, it might skip the next element
- Use while loop instead!
- If you use popleft(), it will be O(1) instead of O(n) for pop, but you have to initialize the self.data with deque() instead of list()
'''