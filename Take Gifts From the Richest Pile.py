# https://leetcode.com/problems/take-gifts-from-the-richest-pile/?envType=daily-question&envId=2024-12-12
# Take Gifts From the Richest Pile

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for i in range(k):

            gifts.sort(reverse=True)

            gifts[0] = int(math.sqrt(gifts[0]))

        return sum(gifts)