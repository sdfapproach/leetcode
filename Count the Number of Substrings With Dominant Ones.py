# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/?envType=daily-question&envId=2025-11-15
# Count the Number of Substrings With Dominant Ones

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        n = len(s)
        nums = [1 if c == '1' else 0 for c in s]

        maxZero = int((math.isqrt(1 + 4*n) - 1) // 2)
        ans = 0

        for zero in range(maxZero + 1):
            z2 = zero * zero

            l = 0
            count0 = 0
            count1 = 0
            lastBad = -1

            for r in range(n):
                if nums[r] == 0:
                    count0 += 1
                else:
                    count1 += 1

                while l < r:
                    if nums[l] == 0:
                        if count0 > zero:
                            count0 -= 1
                            lastBad = l
                            l += 1
                            continue
                        else:
                            break
                    else:
                        if count1 - 1 >= z2:
                            count1 -= 1
                            l += 1
                            continue
                        else:
                            break

                if count0 == zero and count1 >= z2:
                    ans += (l - lastBad)

        return ans