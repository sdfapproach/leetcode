# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/?envType=daily-question&envId=2026-11-09
# Find Servers That Handled Most Number of Requests

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        
        available = list(range(k))
        heapq.heapify(available)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            while busy and busy[0][0] <= time:
                end, server = heapq.heappop(busy)

                idx = i + (server - i) % k
                heapq.heappush(available, idx)

            if not available:
                continue

            while available and available[0] < i:
                idx = heapq.heappop(available)
                heapq.heappush(available, idx + k)

            server = heapq.heappop(available) % k

            count[server] += 1

            heapq.heappush(
                busy, (time + load[i], server)
            )

        max_count = max(count)

        return [
            i for i in range(k)
            if count[i] == max_count
        ]