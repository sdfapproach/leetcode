# https://leetcode.com/problems/path-crossing/description/?envType=daily-question&envId=2023-12-23
# Path Crossing

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # point = [0, 0]
        # points = [[0, 0]]

        # def move(d):
        #     new_point = []
        #     if d == 'N':
        #         new_point.append(point[0])
        #         new_point.append(point[1] + 1)
        #     if d == 'S':
        #         new_point.append(point[0])
        #         new_point.append(point[1] - 1)
        #     if d == 'E':
        #         new_point.append(point[0] + 1)
        #         new_point.append(point[1])
        #     if d == 'W':
        #         new_point.append(point[0] - 1)
        #         new_point.append(point[1])
        #     points.append(new_point)
        #     point[0] = new_point[0]
        #     point[1] = new_point[1]

        # for m in path:
        #     move(m)
        #     for item in points[:len(points)-1]:
        #         print(item, point)
        #         if item[0] == point[0] and item[1] == point[1]:
        #             return True

        # return False

        point = (0, 0)
        points = {point}

        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

        for move in path:
            dx, dy = directions[move]
            point = (point[0] + dx, point[1] + dy)

            if point in points:
                return True

            points.add(point)

        return False