class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in range(len(strs)):
            sorted_strs = "".join(sorted(strs[i]))
            if sorted_strs not in anagram_dict:
                anagram_dict[sorted_strs] = [strs[i]]
            else:
                anagram_dict[sorted_strs].append(strs[i])
        anagram_list = list(anagram_dict.values())
        return anagram_list