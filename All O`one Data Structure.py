# https://leetcode.com/problems/all-oone-data-structure/?envType=daily-question&envId=2024-09-29
# All O`one Data Structure

class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    # def __init__(self):
    #     self.keys = {}

    # def inc(self, key: str) -> None:

    #     if not self.keys:
    #         self.max_key = key
    #         self.min_key = key

    #     if key in self.keys:
    #         self.keys[key] += 1
            
    #     else:
    #         self.keys[key] = 1

    #     return None

    # def dec(self, key: str) -> None:

    #     if self.keys[key] <= 1:
    #         del(self.keys[key])
    #     else:
    #         self.keys[key] -= 1

            
    #     return None

    # def getMaxKey(self) -> str:

    #     if not self.keys:
    #         return ""

    #     return "{}".format(max(self.keys, key=self.keys.get))

    # def getMinKey(self) -> str:

    #     if not self.keys:
    #         return ""

    #     return "{}".format(min(self.keys, key=self.keys.get))

    def __init__(self):
        self.keys = {}
        self.count_map = {}
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.count_map[node.count]

    def _add_node_after(self, new_node, prev_node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        self.count_map[new_node.count] = new_node

    def inc(self, key: str) -> None:
        if key in self.keys:
            count = self.keys[key]
            self.keys[key] += 1
            current_node = self.count_map[count]
            next_count = count + 1

            if next_count not in self.count_map:
                new_node = Node(next_count)
                self._add_node_after(new_node, current_node)
            self.count_map[next_count].keys.add(key)

            current_node.keys.remove(key)
            if not current_node.keys:
                self._remove_node(current_node)
        else:
            self.keys[key] = 1
            if 1 not in self.count_map:
                new_node = Node(1)
                self._add_node_after(new_node, self.head)
            self.count_map[1].keys.add(key)

    def dec(self, key: str) -> None:
        count = self.keys[key]
        current_node = self.count_map[count]
        current_node.keys.remove(key)

        if count == 1:
            del self.keys[key]
        else:
            self.keys[key] -= 1
            prev_count = count - 1
            if prev_count not in self.count_map:
                new_node = Node(prev_count)
                self._add_node_after(new_node, current_node.prev)
            self.count_map[prev_count].keys.add(key)

        if not current_node.keys:
            self._remove_node(current_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()