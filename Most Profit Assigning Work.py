# https://leetcode.com/problems/most-profit-assigning-work/?envType=daily-question&envId=2024-06-18
# Most Profit Assigning Work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        # total = 0

        # for w in worker:

        #     money = 0

        #     for i, diff in enumerate(difficulty):
                
        #         if diff <= w and money <= profit[i]:
        #             money = profit[i]

        #     if money > 0:
        #         total += money

        # return total

        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        j = 0
        total_profit = 0
        
        for ability in worker:
            while j < len(jobs) and jobs[j][0] <= ability:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            total_profit += max_profit
        
        return total_profit