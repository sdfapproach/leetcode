# https://leetcode.com/problems/implement-queue-using-stacks/?envType=daily-question&envId=2024-01-29
# Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item

    def peek(self) -> int:
        return self.queue[0]        

    def empty(self) -> bool:
        if len(self.queue) < 1:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()