# https://leetcode.com/problems/number-of-equivalent-domino-pairs/?envType=daily-question&envId=2025-05-04
# Number of Equivalent Domino Pairs

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        sorted_dominoes = [tuple(sorted(domino)) for domino in dominoes]
    
        counter = Counter(sorted_dominoes)
        
        count = 0

        for freq in counter.values():
            count += (freq * (freq - 1)) // 2
        
        return count