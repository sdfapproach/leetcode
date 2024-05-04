# https://leetcode.com/problems/boats-to-save-people/?envType=daily-question&envId=2024-05-04
# Boats to Save People

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        count = 0

        people.sort(reverse=True)

        f, b = 0, len(people)-1

        while f <= b:

            if people[f] + people[b] <= limit:
                count += 1
                f += 1
                b -= 1
            else:
                count += 1
                f += 1

        return count