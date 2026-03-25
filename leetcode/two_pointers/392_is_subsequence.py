# Problem: 392. Is Subsequence
# Time: O(n)
# Space: O(1)
# URL: https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        start_t = 0
        end_t = len(t) - 1
        end = len(s) - 1
        if end > end_t:
            return False
        while start <= end:
            if start_t > end_t:
                return False
            if s[start] == t[start_t]:
                start += 1
                start_t += 1
                continue
            start_t += 1
        return True
    
'''
Notes
- You always have to think of cases where both array's lenths are zero or one.
- There is a case where s length is longer than t
- You can just make the while loop like while start < len(s) and start_t < len(t):
'''
