# Problem: 345. Reverse Vowels of a String
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        order = []
        s = list(s)
        for ch in range(len(s)):
            if s[ch].lower() in 'aeiou':
                order.append(s[ch])
        for ch in range(len(s)):
            if s[ch].lower() in 'aeiou':
                s[ch] = order.pop()
        s = ''.join(s)
        return s

'''
Notes
- Rather then checking vowels like s[i].lower() == 'a' or s[i].lower() == 'e' ... we can use if s[i].lower() in 'aeiou'
- String is immutable, so we need to convert it to a list to swap characters
- You can also use two pointers to swap characters
'''