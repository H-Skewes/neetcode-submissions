class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        if sorted(list_t) == sorted(list_s):
            return True
        else:
            return False        