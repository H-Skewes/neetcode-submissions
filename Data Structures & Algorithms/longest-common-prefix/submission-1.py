class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        smalleststrs = min(strs, key=len)

        for i in range(len(smalleststrs)):
            for j in strs:
                if j[i] != smalleststrs[i]:
                    return res
            res += smalleststrs[i]
        return res
