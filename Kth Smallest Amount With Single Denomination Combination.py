# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/?envType=daily-question&envId=2026-08-21
# Kth Smallest Amount With Single Denomination Combination

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        
        coins.sort()
        filtered = []

        for coin in coins:
            if not any(coin % x == 0 for x in filtered):
                filtered.append(coin)

        coins = filtered
        m = len(coins)

        def count(x):
            total = 0

            for mask in range(1, 1 << m):
                lcm = 1
                bits = 0

                for i in range(m):
                    if mask & (1 << i):
                        bits += 1

                        lcm = lcm * coins[i] // gcd(lcm, coins[i])

                        if lcm > x:
                            break

                if lcm > x:
                    continue

                if bits % 2:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left