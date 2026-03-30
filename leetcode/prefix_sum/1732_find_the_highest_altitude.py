# Problem: 1732. Find the Highest Altitude
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for i in range(len(gain)):
            alt.append(alt[i] + gain[i])
        return max(alt)