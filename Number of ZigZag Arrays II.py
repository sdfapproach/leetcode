# https://leetcode.com/problems/number-of-zigzag-arrays-ii/?envType=daily-question&envId=2026-06-24
# Number of ZigZag Arrays II

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        
        MOD = 10**9 + 7
        m = r - l + 1

        if m == 1:
            return 1 if n == 1 else 0

        def generate(cnt):
            terms = [m]

            if cnt == 1:
                return terms

            up = [0] * m
            down = [0] * m

            for v in range(m):
                up[v] = v
                down[v] = m - 1 - v

            terms.append((sum(up) + sum(down)) % MOD)

            for _ in range(3, cnt + 1):
                new_up = [0] * m
                new_down = [0] * m

                prefix = 0
                for v in range(m):
                    new_up[v] = prefix
                    prefix = (prefix + down[v]) % MOD

                suffix = 0
                for v in range(m - 1, -1, -1):
                    new_down[v] = suffix
                    suffix = (suffix + up[v]) % MOD

                up, down = new_up, new_down
                terms.append((sum(up) + sum(down)) % MOD)

            return terms

        def berlekamp_massey(s):
            C = [1]
            B = [1]
            L = 0
            m_bm = 1
            b = 1

            for i in range(len(s)):
                d = s[i]
                for j in range(1, L + 1):
                    d = (d + C[j] * s[i - j]) % MOD

                if d == 0:
                    m_bm += 1
                    continue

                T = C[:]
                coef = d * pow(b, MOD - 2, MOD) % MOD

                while len(C) < len(B) + m_bm:
                    C.append(0)

                for j in range(len(B)):
                    C[j + m_bm] = (C[j + m_bm] - coef * B[j]) % MOD

                if 2 * L <= i:
                    L = i + 1 - L
                    B = T
                    b = d
                    m_bm = 1
                else:
                    m_bm += 1

            return [(-C[i]) % MOD for i in range(1, L + 1)]

        def linear_rec(init, rec, k):
            d = len(rec)

            if k < len(init):
                return init[k]

            def combine(a, b):
                res = [0] * (2 * d)

                for i in range(d):
                    for j in range(d):
                        res[i + j] = (res[i + j] + a[i] * b[j]) % MOD

                for i in range(2 * d - 2, d - 1, -1):
                    for j in range(1, d + 1):
                        res[i - j] = (res[i - j] + res[i] * rec[j - 1]) % MOD

                return res[:d]

            pol = [1] + [0] * (d - 1)

            if d == 1:
                e = [rec[0]]
            else:
                e = [0, 1] + [0] * (d - 2)

            while k:
                if k & 1:
                    pol = combine(pol, e)
                e = combine(e, e)
                k >>= 1

            ans = 0
            for i in range(d):
                ans = (ans + pol[i] * init[i]) % MOD

            return ans

        need = 4 * m + 20
        terms = generate(need)

        if n <= len(terms):
            return terms[n - 1]

        rec = berlekamp_massey(terms)

        return linear_rec(terms[:len(rec)], rec, n - 1)