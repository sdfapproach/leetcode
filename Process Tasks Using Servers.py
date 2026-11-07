# https://leetcode.com/problems/process-tasks-using-servers/?envType=daily-question&envId=2026-11-07
# Process Tasks Using Servers

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []

        answer = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                end, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            weight, idx = heapq.heappop(available)
            answer.append(idx)

            heapq.heappush(busy, (time + task, weight, idx))

        return answer