# https://leetcode.com/problems/rabbits-in-forest/?envType=daily-question&envId=2025-04-20
# Rabbits in Forest

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        answer_counts = Counter(answers)
        total_rabbits = 0
        
        for answer, count in answer_counts.items():
            total_rabbits += math.ceil(count / (answer + 1)) * (answer + 1)
        
        return total_rabbits