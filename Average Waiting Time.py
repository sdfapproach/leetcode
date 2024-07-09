# https://leetcode.com/problems/average-waiting-time/?envType=daily-question&envId=2024-07-09
# Average Waiting Time

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        time = 0
        wating = 0

        for customer in customers:

            time = max(time, customer[0])
            
            wating += time + customer[1] - customer[0]

            time += customer[1]

        return wating / len(customers)