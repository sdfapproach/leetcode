# https://leetcode.com/problems/rotating-the-box/?envType=daily-question&envId=2024-11-23
# Rotating the Box

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        col = len(box)
        row = len(box[0])

        rotated_box = [['.' for j in range(col)] for i in range(row)]

        for i in range(row):

            for j in range(col):

                rotated_box[i][j] = box[-(j+1)][i]

        for i in range(col):

            top_stone = None

            for j in range(row):

                if top_stone is None and rotated_box[j][i] == "#":
                    top_stone = j
                elif rotated_box[j][i] == "*":
                    top_stone = None
                elif top_stone is not None and rotated_box[j][i] == ".":
                    rotated_box[top_stone][i] = "."
                    rotated_box[j][i] = "#"

                    if j < len(rotated_box) and rotated_box[top_stone+1][i] == "#":
                        top_stone += 1
                    else:
                        top_stone = None

        return rotated_box