# https://leetcode.com/problems/block-placement-queries/submissions/?envType=daily-question&envId=2026-05-30
# Block Placement Queries

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, v):
        i += 1
        while i <= self.n:
            self.tree[i] += v
            i += i & -i

    def sum(self, i):
        if i < 0:
            return 0
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length())

        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]
            bit >>= 1

        return idx


class SegTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.tree = [0] * (self.size * 2)

    def update(self, idx, val):
        idx += self.size
        self.tree[idx] = val
        idx //= 2

        while idx:
            self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])
            idx //= 2

    def query(self, l, r):
        if l > r:
            return 0

        l += self.size
        r += self.size
        res = 0

        while l <= r:
            if l % 2 == 1:
                res = max(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = max(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2

        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        coords = sorted(set(q[1] for q in queries))
        idx = {x: i for i, x in enumerate(coords)}

        n = len(coords)
        bit = Fenwick(n)
        seg = SegTree(n)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                xi = idx[x]

                left_count = bit.sum(xi - 1)
                total_count = bit.sum(n - 1)

                if left_count == 0:
                    prev = 0
                else:
                    prev_idx = bit.kth(left_count)
                    prev = coords[prev_idx]

                if left_count == total_count:
                    nxt = None
                else:
                    nxt_idx = bit.kth(left_count + 1)
                    nxt = coords[nxt_idx]

                bit.add(xi, 1)

                seg.update(xi, x - prev)

                if nxt is not None:
                    seg.update(idx[nxt], nxt - x)

            else:
                _, x, sz = q

                import bisect
                pos = bisect.bisect_right(coords, x) - 1

                best = seg.query(0, pos)

                cnt = bit.sum(pos)
                if cnt == 0:
                    last = 0
                else:
                    last_idx = bit.kth(cnt)
                    last = coords[last_idx]

                best = max(best, x - last)

                ans.append(best >= sz)

        return ans