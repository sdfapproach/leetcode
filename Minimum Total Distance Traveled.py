# https://leetcode.com/problems/minimum-total-distance-traveled/?envType=daily-question&envId=2024-10-31
# Minimum Total Distance Traveled

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        robot.sort()
        factory.sort()
        
        def assign_robots(curr_pos: int, robot_idx: int, memo: dict) -> int:
            if robot_idx == len(robot):
                return 0
                
            state = (curr_pos, robot_idx)
            if state in memo:
                return memo[state]
                
            result = float('inf')
            if curr_pos + 1 < len(factory):
                result = assign_robots(curr_pos + 1, robot_idx, memo)
                
            robots_assigned = 0
            curr_distance = 0
            
            while (robot_idx + robots_assigned < len(robot) and 
                robots_assigned < factory[curr_pos][1]):
                curr_distance += abs(robot[robot_idx + robots_assigned] - 
                                factory[curr_pos][0])
                robots_assigned += 1
                
                if curr_pos + 1 < len(factory):
                    next_distance = assign_robots(curr_pos + 1, 
                                            robot_idx + robots_assigned, 
                                            memo)
                    if next_distance != float('inf'):
                        result = min(result, curr_distance + next_distance)
                else:
                    if robot_idx + robots_assigned == len(robot):
                        result = min(result, curr_distance)
                        
            memo[state] = result

            return result
            
        memo = {}

        return assign_robots(0, 0, memo)