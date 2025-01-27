# https://leetcode.com/problems/course-schedule-iv/?envType=daily-question&envId=2025-01-27
# Course Schedule IV

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachability = [[False] * numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            reachability[pre][course] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachability[i][k] and reachability[k][j]:
                        reachability[i][j] = True

        answer = []
        for u, v in queries:
            answer.append(reachability[u][v])

        return answer