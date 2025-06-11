# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/?envType=daily-question&envId=2025-06-11
# Maximum Difference Between Even and Odd Frequency II

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def get_status(cnt_a: int, cnt_b: int) -> int:
            return ((cnt_a % 2) << 1) | (cnt_b % 2)

        n = len(s)
        ans = -math.inf
        
        char_set = "01234"

        for a in char_set:
            for b in char_set:
                if a == b:
                    continue

                best = [math.inf] * 4

                cnt_a, cnt_b = 0, 0
                prev_a, prev_b = 0, 0 
                left = -1

                for right in range(n):
                    if s[right] == a:
                        cnt_a += 1
                    elif s[right] == b:
                        cnt_b += 1

                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = get_status(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)

                        left += 1
                        if s[left] == a:
                            prev_a += 1
                        elif s[left] == b:
                            prev_b += 1
                    
                    right_status = get_status(cnt_a, cnt_b)
                    
                    target_status = right_status ^ 0b10  # 2

                    if best[target_status] != math.inf:
                        current_diff = (cnt_a - cnt_b) - best[target_status]
                        ans = max(ans, current_diff)

        return ans if ans != -math.inf else -1