# Problem: 1207. Unique Number of Occurrences
# Time: O(n^2)
# Space: O(n)
# URL: https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = set(arr)
        unique = list(unique)
        count = [0] * len(unique)
        for i in arr:
            j = unique.index(i)
            count[j] += 1
        return len(count) == len(set(count))
    
'''
Notes
- If you want to add a single element to set, you can use set.add() method
- If you want to add multiple elements to set, you can use set.update() method
- You can make it faster using dictionary to count the occurrences of each number in arr.
    - dictionary.get() method can be used to get the value of a key in dictionary. Example) count.get(i, 0) + 1
    - dictionary.values() method can be used to get the values of all keys in dictionary. Example) count.values()
'''