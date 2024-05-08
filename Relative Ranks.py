# https://leetcode.com/problems/relative-ranks/?envType=daily-question&envId=2024-05-08
# Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        # sorted_score = sorted(score, reverse=True)

        # rank = []

        # for num in score:

        #     rank.append(sorted_score.index(num))

        # for i in range(len(rank)):
        #     if rank[i] == 0:
        #         rank[i] = "Gold Medal"
        #     elif rank[i] == 1:
        #         rank[i] = "Silver Medal"
        #     elif rank[i] == 2:
        #         rank[i] = "Bronze Medal"
        #     else:
        #         rank[i] = str(rank[i]+1)

        # return rank

        indexed_scores = [(score[i], i) for i in range(len(score))]
        indexed_scores.sort(reverse=True, key=lambda x: x[0])

        result = [''] * len(score)

        for rank, (score, idx) in enumerate(indexed_scores):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)

        return result