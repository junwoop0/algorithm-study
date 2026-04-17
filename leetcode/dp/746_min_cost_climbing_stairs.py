# Problem: 746. Min Cost Climbing Stairs
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        dp = [0] * length
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,length):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[length-1], dp[length-2])
    
    
'''
Notes
- You can to make a list of the minimum cost to get to each step
- You can decrease the space complexity to O(1) by keeping track of the last two values instead of the whole list.
'''