# Problem: 2390. Removing Stars From a String
# Time:
# Space:
# URL: https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        ans = []
        for ch in s:
            if ch == "*":
                ans.pop()
            else:
                ans.append(ch)
        return "".join(ans)
    
'''
Notes
- pop() makes the elements in the list shift to the left.
- You can make a new list for the result and append the characters to it, but it will take O(n) space.
'''