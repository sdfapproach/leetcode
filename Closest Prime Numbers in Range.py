# https://leetcode.com/problems/closest-prime-numbers-in-range/?envType=daily-question&envId=2025-03-07
# Closest Prime Numbers in Range

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(right**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
        
        primes = [num for num in range(left, right + 1) if sieve[num]]
        
        if len(primes) < 2:
            return [-1, -1]
        
        best_diff = float('inf')
        best_pair = [-1, -1]
        
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < best_diff:
                best_diff = diff
                best_pair = [primes[i - 1], primes[i]]
                if best_diff == 1:
                    return best_pair
        
        return best_pair