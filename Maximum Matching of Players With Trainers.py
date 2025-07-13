# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/?envType=daily-question&envId=2025-07-13
# Maximum Matching of Players With Trainers

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        
        p = t = 0
        matches = 0
        n, m = len(players), len(trainers)
        
        while p < n and t < m:
            if players[p] <= trainers[t]:
                matches += 1
                p += 1
                t += 1
            else:
                t += 1
        
        return matches