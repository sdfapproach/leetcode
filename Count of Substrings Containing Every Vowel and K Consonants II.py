# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/?envType=daily-question&envId=2025-03-10
# Count of Substrings Containing Every Vowel and K Consonants II

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        n = len(word)
        vowels = set('aeiou')
        
        prefixCons = [0] * (n + 1)
        for i in range(n):
            prefixCons[i+1] = prefixCons[i] + (0 if word[i] in vowels else 1)
        
        next_occ = {v: [n] * (n + 1) for v in vowels}
        for v in vowels:
            next_occ[v][n] = n
            for i in range(n-1, -1, -1):
                if word[i] == v:
                    next_occ[v][i] = i
                else:
                    next_occ[v][i] = next_occ[v][i+1]
        
        
        ans = 0
        for i in range(n):
            target = prefixCons[i] + k
            p_left = bisect.bisect_left(prefixCons, target, i+1, n+1)
            if p_left == n+1 or prefixCons[p_left] != target:
                continue
            
            p_right = bisect.bisect_right(prefixCons, target, i+1, n+1) - 1
            
            j_low_consonant = p_left - 1
            j_high_consonant = p_right - 1
            
            j_vowel = 0
            valid = True
            for v in vowels:
                if next_occ[v][i] == n:
                    valid = False
                    break
                j_vowel = max(j_vowel, next_occ[v][i])
            if not valid:
                continue
            
            j_low = max(j_low_consonant, j_vowel)
            j_high = j_high_consonant
            
            if j_low <= j_high:
                ans += (j_high - j_low + 1)
        
        return ans