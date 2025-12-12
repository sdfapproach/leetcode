# https://leetcode.com/problems/count-mentions-per-user/?envType=daily-question&envId=2025-12-12
# Count Mentions Per User

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        
        mentions = [0] * numberOfUsers

        offline_until = [-1] * numberOfUsers

        events.sort(key=lambda e: (int(e[1]), 0 if e[0] == "OFFLINE" else 1))

        def is_online(u, time):
            return offline_until[u] == -1 or offline_until[u] <= time

        for event in events:
            etype = event[0]
            time = int(event[1])

            for u in range(numberOfUsers):
                if offline_until[u] != -1 and offline_until[u] <= time:
                    offline_until[u] = -1

            if etype == "OFFLINE":
                user = int(event[2])
                offline_until[user] = time + 60

            else:
                mentions_str = event[2].split()

                for token in mentions_str:
                    if token == "ALL":
                        for u in range(numberOfUsers):
                            mentions[u] += 1

                    elif token == "HERE":
                        for u in range(numberOfUsers):
                            if is_online(u, time):
                                mentions[u] += 1

                    else:
                        u = int(token[2:])
                        mentions[u] += 1

        return mentions