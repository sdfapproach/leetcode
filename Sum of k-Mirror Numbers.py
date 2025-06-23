# https://leetcode.com/problems/sum-of-k-mirror-numbers/?envType=daily-question&envId=2025-06-23
# Sum of k-Mirror Numbers

class Solution:
    def kMirror(self, k, n):
        
        def mirror(n, base, odd):
            result = n
            if odd:
                n //= base
            while n:
                result = result*base+n%base
                n //= base
            return result

        def num_gen(base):
            prefix_num, total = [1]*2, [base]*2
            odd = 1
            while True:
                x = mirror(prefix_num[odd], base, odd)
                prefix_num[odd] += 1
                if prefix_num[odd] == total[odd]:
                    total[odd] *= base
                    odd ^= 1
                yield x

        def reverse(n, base):
            result = 0
            while n:
                result = result*base+n%base
                n = n//base
            return result

        def mirror_num(gen, base):
            while True:
                x = next(gen)
                if x == reverse(x, base):
                    break
            return x

        base1, base2 = k, 10  # (10, k) is slower
        gen = num_gen(base1)

        return sum(mirror_num(gen, base2) for _ in range(n))