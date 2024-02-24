# https://leetcode.com/problems/find-all-people-with-secret/?envType=daily-question&envId=2024-02-24
# Find All People With Secret

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings_by_time = defaultdict(list)
        for x, y, time in meetings:
            meetings_by_time[time].append((x, y))

        secret_holders = {0, firstPerson}

        for time in sorted(meetings_by_time.keys()):
            while True:
                new_holders = set()
                for x, y in meetings_by_time[time]:
                    if x in secret_holders or y in secret_holders:
                        new_holders.add(x)
                        new_holders.add(y)

                if new_holders.issubset(secret_holders):
                    break

                secret_holders.update(new_holders)

        return list(secret_holders)