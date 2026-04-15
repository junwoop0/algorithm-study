# Problem: 1137. N-th Tribonacci Number
# Time:
# Space:
# URL: https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    val = [0]*38

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        if (self.val[n] != 0):
            return self.val[n]
        self.val[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.val[n]

'''
Notes
- Use memoization to reduce runtime.
'''
