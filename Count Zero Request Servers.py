# https://leetcode.com/problems/count-zero-request-servers/?envType=daily-question&envId=2026-11-06
# Count Zero Request Servers

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(
            enumerate(queries),
            key=lambda q: q[1]
        )

        count = [0] * (n + 1)
        active = 0

        left = 0
        right = 0

        answer = [0] * len(queries)

        for idx, q in sorted_queries:

            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if count[server] == 0:
                    active += 1

                count[server] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            answer[idx] = n - active

        return answer