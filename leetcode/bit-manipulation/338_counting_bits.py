# Problem: 338. Counting Bits
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0, 1]
        temp = 0
        b = 0
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        for i in range(2, n+1):
            if i % (2**(b+1)) == 0:
                b += 1
            ans.append(ans[i - (2**b)] + 1)
        return ans

'''
Notes
- You can also solve it by dividing the cases into even and odd numbers.
'''