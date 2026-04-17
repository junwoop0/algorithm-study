# Problem: 374. Guess Number Higher or Lower
# Time: O(log n)
# Space: O(1)
# URL: https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = int((left + right) / 2)
            if right - left < 3:
                break
            if guess(mid) == -1:
                right = mid
            elif guess(mid) == 1:
                left = mid
            else:
                return mid
        while guess(mid) != 0:
            if guess(mid) == -1:
                mid -= 1
            if guess(mid) == 1:
                mid += 1
        return mid
    
'''
Notes
- Make the range by using left and right, and find the middle point.
'''
