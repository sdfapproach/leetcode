# https://leetcode.com/problems/best-sightseeing-pair/?envType=daily-question&envId=2024-12-27
# Best Sightseeing Pair

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        score = 0
        
        # for i in range(len(values)):
        #     for j in range(i+1, len(values)):
        #         score = max(score, (values[i] + values[j] + i - j))

        # return score

        max_i = values[0]

        for j in range(1, len(values)):
            score = max(score, max_i + values[j] - j)
            max_i = max(max_i, values[j] + j)
        
        return score