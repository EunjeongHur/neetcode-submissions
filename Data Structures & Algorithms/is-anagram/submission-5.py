class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counting = {}

        for char in s:
            counting[char] = counting.get(char, 0) + 1
        
        for char in t:
            counting[char] = counting.get(char, 0) - 1
            if counting[char] < 0:
                return False

        return True