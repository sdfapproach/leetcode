# https://leetcode.com/problems/task-scheduler/?envType=daily-question&envId=2024-03-19
# Task Scheduler

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # work = 0

        # count = collections.Counter(tasks)

        # cycle = sorted(list(set(tasks)))

        # num = n

        # while len(cycle) > 0:

        #     for n in cycle:

        #         if count[n] > 1:
        #             count[n] -= 1
        #             work += 1

        #             idle = (num +1 - len(cycle))
        #             if idle > 0:
        #                 work += (idle)/2
                    
        #         elif count[n] == 1:
        #             work += 1
        #             cycle.remove(n)

        # return int(work)

        task_counts = Counter(tasks)
        max_task_count = max(task_counts.values())
        tasks_with_max_count = sum(count == max_task_count for count in task_counts.values())

        part_count = max_task_count - 1
        part_length = n - (tasks_with_max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_task_count * tasks_with_max_count
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles