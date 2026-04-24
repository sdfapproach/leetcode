# https://leetcode.com/problems/furthest-point-from-origin/?envType=daily-question&envId=2026-04-24
# Furthest Point From Origin

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        L = moves.count('L')
        R = moves.count('R')
        U = moves.count('_')
        
        return abs(L - R) + U