class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(t)) == sorted(list(s)):
            return True
        else:
            return False        