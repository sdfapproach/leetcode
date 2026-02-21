# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/?envType=daily-question&envId=2026-02-21
# Prime Number of Set Bits in Binary Representation

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        count = 0

        def is_prime(n):

            if n < 2:
                return False

            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        for n in range(left, right+1):
            if is_prime(n.bit_count()):
                count += 1

        return count