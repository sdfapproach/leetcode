# https://leetcode.com/problems/letter-tile-possibilities/?envType=daily-question&envId=2025-02-17
# Letter Tile Possibilities

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        freq = Counter(tiles)
        
        def dfs() -> int:
            count = 0
            for letter in freq:
                if freq[letter] > 0:
                    count += 1
                    freq[letter] -= 1
                    count += dfs()
                    freq[letter] += 1
            return count
        
        return dfs()