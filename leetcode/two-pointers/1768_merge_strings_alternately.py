# Problem: 1768. Merge Strings Alternately
# Time: O(n + m)
# Space: O(n + m)
# URL: https://leetcode.com/problems/merge-strings-alternately/description/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        a = len(word1)
        b = len(word2)
        if a >= b:
            for i in range(b):
                ans.append(word1[i])
                ans.append(word2[i])
            for i in range(b, a):
                ans.append(word1[i])
        else:
            for i in range(a):
                ans.append(word1[i])
                ans.append(word2[i])
            for i in range(a, b):
                ans.append(word2[i])
        ans = ''.join(ans)
        return ans
    
'''
Note
If you want to connect elements of a list into a string, you can use the join() method.
    - Ex) my_list = ['H', 'e', 'l', 'l', 'o']
          result = ''.join(my_list)  # result will be 'Hello'
'''
