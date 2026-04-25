# Problem: 151. Reverse Words in a String
# Time: O(n)
# Space: O(n)
# URL: https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        s.reverse()
        s = ' '.join(s)
        return s

'''
Notes
- strip() is used to remove leading and trailing spaces
    - ex) '  hello world  '.strip() -> 'hello world'
- split() is used to split a string into a list of words
    - ex) 'hello world'.split() -> ['hello', 'world']
- join() is used to join a list of words into a string
    - ex) ' '.join(['world', 'hello']) -> 'world hello'
- To make integer list into string list, we can use map() function or list comprehension
    - ex) [str(x) for x in [1, 2, 3]] -> ['1', '2', '3']    
    - ex) map(str, [1, 2, 3]) -> ['1', '2', '3']
'''
