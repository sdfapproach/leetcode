# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/?envType=daily-question&envId=2025-06-07
# Lexicographically Minimum String After Removing Stars

class Solution:
    def clearStars(self, s: str) -> str:
        
        char_pos = [[] for _ in range(26)]
        s_list = list(s)
        
        for i, c in enumerate(s_list):
            if c == '*':
                for j in range(26):
                    if char_pos[j]:
                        pos = char_pos[j].pop()
                        s_list[pos] = '*'
                        break
            else:
                char_pos[ord(c) - ord('a')].append(i)
        
        res = []

        for c in s_list:
            if c != '*':
                res.append(c)
        
        return ''.join(res)