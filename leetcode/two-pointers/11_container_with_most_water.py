# Problem: 11. Container With Most Water
# Time: O(n)
# Space: O(1)
# URL: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        ans = 0
        while start < end :
            x = end - start
            y = min(height[start], height[end])
            area = x * y
            if area > ans:
                ans = area
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return ans
