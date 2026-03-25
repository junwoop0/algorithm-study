# Problem: 605. Can Place Flowers
# Time: O(n)
# Space: O(1)
# URL: https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
            
        if flowerbed[0] == 0:
            if (len(flowerbed) == 1):
                n -= 1
                if n == 0:
                    return True
            elif flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
                if n == 0:
                    return True

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0:
                if (flowerbed[i-1] == 0) and (flowerbed[i+1] ==0):
                    n -= 1
                    flowerbed[i] = 1
                    if n == 0:
                        return True

        if flowerbed[len(flowerbed)-1] == 0:
            if flowerbed[len(flowerbed) - 2] == 0:
                flowerbed[(len(flowerbed)-1)] = 1
                n -= 1
                if n == 0:
                    return True

        return False
    

'''
Notes
- Always think of exceptional cases, such as list length is 1 or n is 0
- You can use only one loop to solve this problem
'''
