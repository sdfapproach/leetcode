# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/?envType=daily-question&envId=2026-01-23
# Minimum Pair Removal to Sort Array II

class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.prev = None
        self.next = None
        self.valid = True

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 2:
            return 0
        
        nodes = [Node(x, i) for i, x in enumerate(nums)]
        for i in range(n - 1):
            nodes[i].next = nodes[i+1]
            nodes[i+1].prev = nodes[i]
            
        bad_count = 0
        min_heap = []
        
        for i in range(n - 1):
            current_sum = nodes[i].val + nodes[i+1].val
            heapq.heappush(min_heap, (current_sum, i))
            if nodes[i].val > nodes[i+1].val:
                bad_count += 1
                
        ops = 0
        
        while bad_count > 0:
            if not min_heap:
                break
                
            current_heap_sum, idx = heapq.heappop(min_heap)
            node = nodes[idx]
            
            if not node.valid or node.next is None:
                continue
                
            real_sum = node.val + node.next.val
            if current_heap_sum != real_sum:
                continue
                
            next_node = node.next
            
            if node.prev and node.prev.val > node.val:
                bad_count -= 1
            if node.val > next_node.val:
                bad_count -= 1
            if next_node.next and next_node.val > next_node.next.val:
                bad_count -= 1
                
            new_val = node.val + next_node.val
            node.val = new_val
            
            next_node.valid = False
            node.next = next_node.next
            if node.next:
                node.next.prev = node
                
            if node.prev:
                if node.prev.val > node.val:
                    bad_count += 1
                heapq.heappush(min_heap, (node.prev.val + node.val, node.prev.idx))
                
            if node.next:
                if node.val > node.next.val:
                    bad_count += 1
                heapq.heappush(min_heap, (node.val + node.next.val, node.idx))
                
            ops += 1
            
        return ops