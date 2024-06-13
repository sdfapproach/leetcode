# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/?envType=daily-question&envId=2024-06-13
# Minimum Number of Moves to Seat Everyone

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        seats.sort()
        students.sort()

        count = 0

        for i in range(len(students)):
            count += abs(students[i] - seats[i])

        return count