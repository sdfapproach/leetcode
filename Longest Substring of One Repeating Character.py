# https://leetcode.com/problems/longest-substring-of-one-repeating-character/?envType=daily-question&envId=2026-08-13
# Longest Substring of One Repeating Character

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        
        n = len(s)
        s = list(s)

        size = 1
        while size < n:
            size *= 2

        tree = [None] * (2 * size)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            lc1, rc1, pre1, suf1, best1, len1 = left
            lc2, rc2, pre2, suf2, best2, len2 = right

            pre = pre1
            suf = suf2
            best = max(best1, best2)

            if rc1 == lc2:
                best = max(best, suf1 + pre2)

                if pre1 == len1:
                    pre = len1 + pre2

                if suf2 == len2:
                    suf = len2 + suf1

            return (
                lc1,
                rc2,
                pre,
                suf,
                best,
                len1 + len2
            )

        for i in range(n):
            tree[size + i] = (s[i], s[i], 1, 1, 1, 1)

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[i * 2], tree[i * 2 + 1])

        def update(index, char):
            pos = size + index

            tree[pos] = (char, char, 1, 1, 1, 1)

            pos //= 2

            while pos:
                tree[pos] = merge(
                    tree[pos * 2],
                    tree[pos * 2 + 1]
                )
                pos //= 2

        answer = []

        for index, char in zip(queryIndices, queryCharacters):
            if s[index] != char:
                s[index] = char
                update(index, char)

            answer.append(tree[1][4])

        return answer