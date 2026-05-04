# Problem: 1657. Determine if Two Strings Are Close
# Time: O(n log n)
# Space: O(n)
# URL: https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_count = {}
        word2_count = {}
        for ch in word1:
            word1_count[ch] = word1_count.get(ch, 0) + 1
        for ch in word2:
            word2_count[ch] = word2_count.get(ch, 0) + 1
        return set(word1) == set(word2) and sorted(word1_count.values()) == sorted(word2_count.values())

'''
Notes
- When comparing two sets, order is not considered
- You should use sorted() function to compare the values of two dictionaries, 
because the order of values in dictionary is not guaranteed.
- ord() function can be used to get the ASCII value of a character. 
    - ex) ord('a') -> 97
'''