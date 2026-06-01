# Problem: 2300. Successful Pairs of Spells and Potions
# Time: O(m log n)
# Space: O(1)
# URL: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        pairs = []
        n = len(potions) - 1
        for i in spells:
            start = 0
            end = n
            if i * potions[0] >= success:
                pairs.append(n + 1)
                continue
            if i * potions[n] < success:
                pairs.append(0)
                continue
            while start <= end:
                mid = int((start + end)/2)
                if i * potions[mid] >= success:
                    end = mid - 1
                    # if i * potions[end] < success:
                    #     count = n - end
                    #     break
                else:
                    start = mid + 1
                    # if i * potions[start] >= success:
                    #     count = n - start + 1
                    #     break
            pairs.append(n - start + 1)
        return pairs


'''
Notes
- You don't need break the loop when you find the middle point, just update the start and end,
and after the loop, start will be the index of the first potion that can make the spell successful, so the count will be n - start + 1.
'''