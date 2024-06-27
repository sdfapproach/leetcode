# https://leetcode.com/problems/find-center-of-star-graph/?envType=daily-question&envId=2024-06-27
# Find Center of Star Graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        # if edges[0][0] == edges[1][0]:
        #     return edges[1][0]
        # elif edges[0][0] == edges[1][1]:
        #     return edges[1][1]
        # elif edges[0][1] == edges[1][0]:
        #     return edges[1][0]
        # elif edges[0][1] == edges[1][1]:
        #     return edges[1][1]

         if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]