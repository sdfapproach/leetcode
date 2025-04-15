# https://leetcode.com/problems/count-good-triplets-in-an-array/?envType=daily-question&envId=2025-04-15
# Count Good Triplets in an Array

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)
        
    def update(self, i: int, delta: int):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
            
    def query(self, i: int) -> int:
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        

        n = len(nums1)
        pos2 = [0] * n
        for i, v in enumerate(nums2):
            pos2[v] = i
            
        B = [0] * n
        for i, v in enumerate(nums1):
            B[i] = pos2[v]
            
        L = [0] * n
        bit_left = BIT(n)
        for j in range(n):
            L[j] = bit_left.query(B[j] - 1)
            bit_left.update(B[j], 1)
            
        R = [0] * n
        bit_right = BIT(n)
        for j in range(n - 1, -1, -1):
            R[j] = bit_right.query(n - 1) - bit_right.query(B[j])
            bit_right.update(B[j], 1)
        
        total_triplets = 0
        for j in range(n):
            total_triplets += L[j] * R[j]
        
        return total_triplets