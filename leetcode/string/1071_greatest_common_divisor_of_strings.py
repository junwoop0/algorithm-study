# Problem: 1071. Greatest Common Divisor of Strings
# Time: O((n + m) * min(n, m))
# Space: O(n + m)
# URL: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate = []
        i = 0
        while (i < min(len(str1),len(str2))):
            if (str1[i] == str2[i]):
                candidate.append(str1[i])
                i += 1
            else:
                break
        if (candidate == []):
            return ""
        while (1):
            if ((len(str1) % len(candidate) == 0) and (len(str2) % len(candidate) == 0)):
                a = int(len(str1) / len(candidate))
                b = int(len(str2) / len(candidate))
                ans = ''.join(candidate)
                if ((ans * a == str1) and (ans * b == str2)):
                    return ans
            candidate.pop()
            if candidate == []:
                return ""
            

'''
Notes
- You can multiply a string by an integer to repeat the string that many times.
'''
