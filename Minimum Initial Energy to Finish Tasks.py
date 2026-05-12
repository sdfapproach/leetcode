# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/?envType=daily-question&envId=2026-05-12
# Minimum Initial Energy to Finish Tasks

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
    
        total_initial_energy = 0
        current_energy = 0
        
        for actual, minimum in tasks:
            if current_energy < minimum:
                shortfall = minimum - current_energy
                total_initial_energy += shortfall
                current_energy += shortfall
                
            current_energy -= actual
            
        return total_initial_energy