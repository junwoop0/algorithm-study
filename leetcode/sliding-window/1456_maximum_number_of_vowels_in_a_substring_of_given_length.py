# Problem: 1456. Maximum Number of Vowels in a Substring of Given Length
# Time: O(n)
# Space: O(1)
# URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for i in range(0, k):
            if s[i] in 'aeiou':
                count += 1
        ans = count
        for i in range(0, len(s) - k):
            if s[i] in 'aeiou':
                count -= 1
            if s[i+k] in 'aeiou':
                count += 1
            if count > ans:
                ans = count
        return ans
    
'''
Notes
- You can make if count > ans part to ans = max(ans, count) to make it more concise
- You can make range(0, k) part to range(k)
'''