# https://leetcode.com/problems/time-needed-to-buy-tickets/?envType=daily-question&envId=2024-04-09
# Time Needed to Buy Tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        i = 0
        
        while tickets[k] > 0:
            if tickets[i] > 0:
                tickets[i] -= 1
                time += 1
                if i == k and tickets[k] == 0:
                    break
            
            i = (i + 1) % len(tickets)
        
        return time