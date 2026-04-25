# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/?envType=daily-question&envId=2026-04-25
# Maximize the Distance Between Points on a Square

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        
        def get_pos(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y
                
        A = sorted([get_pos(x, y) for x, y in points])
        N = len(A)
        L = 4 * side
        
        A_ext = A + [a + L for a in A]
        
        def check(D):
            nxt = [2 * N] * (2 * N)
            j = 0
            for i in range(2 * N):
                while j < 2 * N and A_ext[j] - A_ext[i] < D:
                    j += 1
                nxt[i] = j
            
            for i in range(N):
                curr = i
                for _ in range(k):
                    if curr >= 2 * N:
                        break
                    curr = nxt[curr]
                if curr <= i + N:
                    return True
            return False

        low = 1
        high = L // k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans