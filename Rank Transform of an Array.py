# https://leetcode.com/problems/rank-transform-of-an-array/?envType=daily-question&envId=2024-10-02
# Rank Transform of an Array

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        arr_idx = [[num, i] for i, num in enumerate(arr)]
        arr_idx.sort(key = lambda x : x[0])

        rank = 1
        rank_list = [0] * len(arr_idx)

        for i, item in enumerate(arr_idx):

            if i > 0 and item[0] > arr_idx[i-1][0]:
                rank += 1

            rank_list[item[1]] = rank

        return rank_list