# https://leetcode.com/problems/vowel-spellchecker/?envType=daily-question&envId=2025-09-14
# Vowel Spellchecker

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        vowels = set("aeiou")

        def devowel(s: str):
            s = s.lower()
            return ''.join('*' if ch in vowels else ch for ch in s)

        exact = set(wordlist)
        ci = {}
        va = {}

        for w in wordlist:
            lw = w.lower()
            ci.setdefault(lw, w)
            va.setdefault(devowel(w), w)

        ans = []

        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            lq = q.lower()
            if lq in ci:
                ans.append(ci[lq])
                continue
            dq = devowel(q)
            ans.append(va.get(dq, ""))

        return ans