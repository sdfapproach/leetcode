# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/?envType=daily-question&envId=2025-01-14
# Find the Prefix Common Array of Two Arrays

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)
        seen_in_A = set()
        seen_in_B = set()
        prefix_common = []

        for i in range(n):
            seen_in_A.add(A[i])
            seen_in_B.add(B[i])
            common_count = len(seen_in_A.intersection(seen_in_B))
            prefix_common.append(common_count)

        return prefix_common