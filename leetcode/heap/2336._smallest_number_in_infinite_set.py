# Problem: 2336. Smallest Number in Infinite Set
# Time: O(log n)
# Space: O(n)
# URL: https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet:

    def __init__(self):
        self.count = 1
        self.array = []
        self.check = set()


    def popSmallest(self) -> int:
        if not self.array or self.count < self.array[0]:
            ans = self.count
            self.count += 1
            return ans
        else:
            self.check.discard(self.array[0])
            return heapq.heappop(self.array)

    def addBack(self, num: int) -> None:
        if num not in self.check and num < self.count:
            heapq.heappush(self.array, num)
            self.check.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)


'''
Notes
- Emply list cannot be checked by if list is not None, we need to treat empty list as False
    - Example of False: [], 0, '', None, {}
    - But we can't check an empty list as 'if array is False', so we need to check if the list is empty by 'if not array' 
- You have to also remove elements in the set when you pop the smallest element
'''
