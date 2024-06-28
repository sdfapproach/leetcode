# https://leetcode.com/problems/maximum-total-importance-of-roads/?envType=daily-question&envId=2024-06-28
# Maximum Total Importance of Roads

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        importance = defaultdict(int)

        for road in roads:
            importance[road[0]] += 1
            importance[road[1]] += 1

        sorted_cities = sorted(importance.items(), key=lambda x: x[1], reverse=True)
        
        value_assignment = {}
        importance_value = n

        for city, _ in sorted_cities:
            value_assignment[city] = importance_value
            importance_value -= 1
        
        total_importance = 0

        for road in roads:
            total_importance += value_assignment[road[0]] + value_assignment[road[1]]
        
        return total_importance