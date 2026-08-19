# https://leetcode.com/problems/cinema-seat-allocation/?envType=daily-question&envId=2026-08-19
# Cinema Seat Allocation

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reserved = defaultdict(set)

        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved[row].add(seat)

        answer = (n - len(reserved)) * 2

        left = {2, 3, 4, 5}
        middle = {4, 5, 6, 7}
        right = {6, 7, 8, 9}

        for seats in reserved.values():
            left_ok = not (seats & left)
            right_ok = not (seats & right)

            if left_ok and right_ok:
                answer += 2
            elif left_ok or right_ok or not (seats & middle):
                answer += 1

        return answer