# https://leetcode.com/problems/walking-robot-simulation/?envType=daily-question&envId=2024-09-04
# Walking Robot Simulation

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        # x, y = 0, 0
        # longest = [0, 0]

        # heading = 0

        # for move in commands:

        #     if move == -1:

        #         heading += 90

        #         if heading > 360:
        #             heading = 0

        #     elif move == -2:
        #         heading -= 90

        #         if heading < 0:
        #             heading = 270

        #     else:

        #         if heading == 0:
        #             y += move
        #         elif heading == 90:
        #             x += move
        #         elif heading == 180:
        #             y -= move
        #         elif heading == 270:
        #             x -= move
            
        #     if x**2 + y**2 > longest[0]**2 + longest[1]**2:
        #         longest[0] = x
        #         longest[1] = y

        # return longest[0]**2 + longest[1]**2

        x, y = 0, 0
        heading = 0
        longest = 0

        obstacle_set = set(map(tuple, obstacles))

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for move in commands:
            if move == -1:
                heading = (heading + 1) % 4
            elif move == -2:
                heading = (heading - 1) % 4
            else:
                for _ in range(move):
                    next_x = x + direction[heading][0]
                    next_y = y + direction[heading][1]

                    if (next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y

                longest = max(longest, x**2 + y**2)

        return longest