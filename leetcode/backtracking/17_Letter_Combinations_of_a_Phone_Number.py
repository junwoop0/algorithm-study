# Problem: 17. Letter Combinations of a Phone Number
# Time: 
# Space:
# URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        ans = []
        def backtrack(way):
            if len(way) == len(digits):
                print("".join(way))
                ans.append("".join(way))
                return
            
            for j in phone[digits[len(way)]]:
                way.append(j)
                backtrack(way)
                way.pop()
        if not digits:
            return []
        backtrack([])
        return ans