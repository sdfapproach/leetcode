# https://leetcode.com/problems/design-task-manager/?envType=daily-question&envId=2025-09-18
# Design Task Manager

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.info: Dict[int, Tuple[int, int]] = {}
        self.heap: List[Tuple[int, int]] = []
        for userId, taskId, priority in tasks:
            self.info[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.info[taskId]
        self.info[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        self.info.pop(taskId, None)

    def execTop(self) -> int:
        while self.heap:
            npri, ntid = heapq.heappop(self.heap)
            pri, tid = -npri, -ntid
            if tid in self.info and self.info[tid][1] == pri:
                userId, _ = self.info.pop(tid)
                return userId
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()