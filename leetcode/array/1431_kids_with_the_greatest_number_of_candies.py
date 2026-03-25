# Problem: 1431. Kids With the Greatest Number of Candies
# Time: O(n^2)
# Space: O(n)
# URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for i in range(len(candies)):
            a = candies[i] + extraCandies
            m = max(candies)
            if a >= m:
                ans.append(True)
            else:
                ans.append(False)
        return ans
    
'''
Notes
- You can save time by removing the max() function from the loop and just calculating it before the loop.
'''