# https://leetcode.com/problems/design-a-number-container-system/?envType=daily-question&envId=2025-02-08
# Design a Number Container System

class NumberContainers:

    def __init__(self):

        self.index_to_num = {}
        self.num_to_heap = {}

    def change(self, index: int, number: int) -> None:
        
        self.index_to_num[index] = number
        
        if number not in self.num_to_heap:
            self.num_to_heap[number] = []
        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number: int) -> int:
        
        if number not in self.num_to_heap:
            return -1
        
        heap = self.num_to_heap[number]
        while heap and self.index_to_num.get(heap[0]) != number:
            heapq.heappop(heap)
        
        if not heap:
            return -1
        
        return heap[0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)