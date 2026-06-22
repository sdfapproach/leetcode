# https://leetcode.com/problems/maximum-number-of-balloons/?envType=daily-question&envId=2026-06-22
# Maximum Number of Balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        ballons = 0
        
        count = Counter(text)

        ballons = count['b']
        ballons = min(ballons, count['a'])
        ballons = min(ballons, count['l']//2)
        ballons = min(ballons, count['o']//2)
        ballons = min(ballons, count['n'])

        return ballons