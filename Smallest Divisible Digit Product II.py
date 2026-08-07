# https://leetcode.com/problems/smallest-divisible-digit-product-ii/?envType=daily-question&envId=2026-08-07
# Smallest Divisible Digit Product II

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        
        factors = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0),
        }

        need = [0, 0, 0, 0]

        for i, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                need[i] += 1
                t //= p

        if t != 1:
            return "-1"

        def build(req, length):
            a, b, c, d = [max(0, x) for x in req]

            cnt = [0] * 10

            # 5와 7
            cnt[5] = c
            cnt[7] = d

            cnt[8], rem2 = divmod(a, 3)

            cnt[9], rem3 = divmod(b, 2)

            if rem2 == 1 and rem3 == 1:
                cnt[6] += 1

            elif rem2 == 2 and rem3 == 1:
                cnt[2] += 1
                cnt[6] += 1

            else:
                if rem2 == 1:
                    cnt[2] += 1
                elif rem2 == 2:
                    cnt[4] += 1

                if rem3 == 1:
                    cnt[3] += 1

            used = sum(cnt)

            if used > length:
                return None

            cnt[1] = length - used

            return ''.join(
                str(digit) * cnt[digit]
                for digit in range(1, 10)
            )

        n = len(num)

        current = [0, 0, 0, 0]
        zeros = 0

        for ch in num:
            digit = int(ch)

            if digit == 0:
                zeros += 1
            else:
                f = factors[digit]
                for j in range(4):
                    current[j] += f[j]

        if zeros == 0 and all(current[i] >= need[i] for i in range(4)):
            return num

        for i in range(n - 1, -1, -1):
            digit = int(num[i])

            if digit == 0:
                zeros -= 1
            else:
                f = factors[digit]
                for j in range(4):
                    current[j] -= f[j]

            if zeros > 0:
                continue

            for nxt in range(max(1, digit + 1), 10):
                f = factors[nxt]

                req = [
                    need[j] - current[j] - f[j]
                    for j in range(4)
                ]

                suffix = build(req, n - i - 1)

                if suffix is not None:
                    return num[:i] + str(nxt) + suffix

        length = n + 1

        while True:
            candidate = build(need, length)

            if candidate is not None:
                return candidate

            length += 1