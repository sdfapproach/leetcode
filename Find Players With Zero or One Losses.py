# https://leetcode.com/problems/find-players-with-zero-or-one-losses/?envType=daily-question&envId=2024-01-15
# Find Players With Zero or One Losses

from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        # winner = Counter()
        # loser = Counter()

        # for li in matches:
        #     winner[li[0]] += 1
        #     loser[li[1]] += 1
       
        # not_lost = [n for n in winner if n not in loser]
        # set(not_lost)
        # one_lost = [n for n, c in loser.items() if c == 1]

        # not_lost.sort()
        # one_lost.sort()

        # return [not_lost, one_lost]

        winner = Counter()
        loser = Counter()

        for w, l in matches:
            winner[w] += 1
            loser[l] += 1

        not_lost = sorted(list(set(winner) - set(loser)))
        one_lost = sorted([n for n, c in loser.items() if c == 1])

        return [not_lost, one_lost]