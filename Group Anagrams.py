# https://leetcode.com/problems/group-anagrams/?envType=daily-question&envId=2024-02-06
# Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted_strs = ["".join(sorted(n)) for n in strs]
        # group_list = []
        # checked = set()

        # for i, st in enumerate(sorted_strs):
        #     if i in checked:
        #         continue
        #     group = []

        #     for j in range(len(sorted_strs)):
        #         if j in checked:
        #             continue

        #         if st == sorted_strs[j]:
        #             checked.add(j)
        #             group.append(strs[j])

        #     group_list.append(sorted(group))
        
        # return sorted(group_list)

        anagram_map = {}

        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = [s]
            else:
                anagram_map[sorted_str].append(s)

        return list(anagram_map.values())