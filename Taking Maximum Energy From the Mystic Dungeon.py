# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/?envType=daily-question&envId=2025-10-10
# Taking Maximum Energy From the Mystic Dungeon

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        n = len(energy)
        best = float('-inf')
        upto = min(k, n)

        for r in range(upto):
            last = r + ((n - 1 - r) // k) * k
            s = 0
            i = last
            while i >= r:
                s += energy[i]
                if s > best:
                    best = s
                i -= k
        return best