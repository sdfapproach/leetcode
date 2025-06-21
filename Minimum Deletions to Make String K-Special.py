# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/?envType=daily-question&envId=2025-06-21
# Minimum Deletions to Make String K-Special

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        
        freq = Counter(word)
        counts = list(freq.values())
        if not counts:
            return 0
        
        total = len(word)
        max_f = max(counts)
        best_keep = 0
        
        for L in range(1, max_f + 1):
            keep = 0
            upper = L + k
            for f in counts:
                if f >= L:
                    keep += min(f, upper)
            if keep > best_keep:
                best_keep = keep
        
        return total - best_keep