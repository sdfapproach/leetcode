# https://leetcode.com/problems/implement-router/?envType=daily-question&envId=2025-09-20
# Implement Router

class Router:

    def __init__(self, memoryLimit: int):
        self.cap = memoryLimit
        self.q = deque()  # FIFO: holds (source, dest, ts)
        self.live = set() # for duplicate detection
        # dest -> {'arr': [timestamps...], 'head': int}
        self.by_dest = defaultdict(lambda: {"arr": [], "head": 0})

    def _compact_if_needed(self, dest: int) -> None:
        d = self.by_dest[dest]
        arr, head = d["arr"], d["head"]
        if head > 1024 and head * 2 > len(arr):
            d["arr"] = arr[head:]
            d["head"] = 0

    def _remove_front_effects(self) -> None:
        src, dst, ts = self.q.popleft()
        self.live.discard((src, dst, ts))
        d = self.by_dest[dst]
        d["head"] += 1
        self._compact_if_needed(dst)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if self.cap == 0:
            return False

        key = (source, destination, timestamp)
        if key in self.live:
            return False

        if len(self.q) == self.cap:
            self._remove_front_effects()

        self.q.append(key)
        self.live.add(key)
        d = self.by_dest[destination]
        d["arr"].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        src, dst, ts = self.q[0]
        self._remove_front_effects()
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        d = self.by_dest.get(destination)
        if not d:
            return 0
        arr, head = d["arr"], d["head"]
        if head >= len(arr):
            return 0
        lo = bisect_left(arr, startTime, head)
        hi = bisect_right(arr, endTime, head)
        return max(0, hi - lo)
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)