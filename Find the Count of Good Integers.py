# https://leetcode.com/problems/find-the-count-of-good-integers/?envType=daily-question&envId=2025-04-12
# Find the Count of Good Integers

def precompute_factorials(n):
    fact = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] = fact[i-1] * i
    return fact

def count_arrangements(M, n, fact):
    total = fact[n]
    for d in range(10):
        total //= fact[M[d]]
    if M[0] == 0:
        return total
    total0 = fact[n-1]
    total0 //= fact[M[0]-1]
    for d in range(1, 10):
        total0 //= fact[M[d]]
    return total - total0

def exists_half_ordering_even(G, pos, L, r, weights, k):
    if pos == L:
        return (r % k) == 0
    key = (G, pos, r)
    if key in exists_half_ordering_even.memo:
        return exists_half_ordering_even.memo[key]
    for d in range(10):
        if G[d] > 0:
            if pos == 0 and d == 0:
                continue
            new_G = list(G)
            new_G[d] -= 1
            new_G = tuple(new_G)
            new_r = (r + d * weights[pos]) % k
            if exists_half_ordering_even(new_G, pos+1, L, new_r, weights, k):
                exists_half_ordering_even.memo[key] = True
                return True
    exists_half_ordering_even.memo[key] = False
    return False
exists_half_ordering_even.memo = {}

def exists_half_ordering_odd(G, pos, L, r, weights, middle_contrib, k):
    if pos == L:
        return ((r + middle_contrib) % k) == 0
    key = (G, pos, r, middle_contrib)
    if key in exists_half_ordering_odd.memo:
        return exists_half_ordering_odd.memo[key]
    for d in range(10):
        if G[d] > 0:
            if pos == 0 and d == 0:
                continue
            new_G = list(G)
            new_G[d] -= 1
            new_G = tuple(new_G)
            new_r = (r + d * weights[pos]) % k
            if exists_half_ordering_odd(new_G, pos+1, L, new_r, weights, middle_contrib, k):
                exists_half_ordering_odd.memo[key] = True
                return True
    exists_half_ordering_odd.memo[key] = False
    return False
exists_half_ordering_odd.memo = {}

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        fact = precompute_factorials(n)
        total_ans = 0
        if n % 2 == 0:
            L = n // 2
            def gen_half(i, remain, current):
                if i == 10:
                    if remain == 0:
                        yield tuple(current)
                    return
                for val in range(remain + 1):
                    current.append(val)
                    yield from gen_half(i+1, remain - val, current)
                    current.pop()
            for G in gen_half(0, L, []):
                if G[0] == L:
                    continue
                M = [2*x for x in G]
                weights = []
                for pos in range(L):
                    w = (pow(10, n - pos - 1, k) + pow(10, pos, k)) % k
                    weights.append(w)
                exists_half_ordering_even.memo.clear()
                if exists_half_ordering_even(G, 0, L, 0, tuple(weights), k):
                    total_ans += count_arrangements(M, n, fact)
            return total_ans
        else:
            L = (n - 1) // 2
            def gen_half(i, remain, current):
                if i == 10:
                    if remain == 0:
                        yield tuple(current)
                    return
                for val in range(remain + 1):
                    current.append(val)
                    yield from gen_half(i+1, remain - val, current)
                    current.pop()
            for G in gen_half(0, L, []):
                for m in range(10):
                    if L == 0 and m == 0:
                        continue
                    if L > 0 and G[0] == L:
                        continue
                    M = [2*x for x in G]
                    M[m] += 1
                    weights = []
                    for pos in range(L):
                        w = (pow(10, n - pos - 1, k) + pow(10, pos, k)) % k
                        weights.append(w)
                    middle_contrib = (m * pow(10, L, k)) % k
                    exists_half_ordering_odd.memo.clear()
                    if exists_half_ordering_odd(G, 0, L, 0, tuple(weights), middle_contrib, k):
                        total_ans += count_arrangements(M, n, fact)
            return total_ans