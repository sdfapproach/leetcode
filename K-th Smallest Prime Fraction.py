# https://leetcode.com/problems/k-th-smallest-prime-fraction/?envType=daily-question&envId=2024-05-10
# K-th Smallest Prime Fraction

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        # fractions = dict()

        # for i in range(len(arr)):
        #     for j in range(i+1, len(arr)):
        #         fractions[arr[i]/arr[j]] = [arr[i],arr[j]]

        # fractions = [[key, value] for key, value in fractions.items()]

        # fractions.sort(key=lambda x: x[0])

        # return fractions[k-1][1]

        heap = []
        n = len(arr)
        for i in range(n - 1):
            heapq.heappush(heap, (arr[i] / arr[n-1], i, n-1))
        
        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            if j - 1 > i:
                heapq.heappush(heap, (arr[i] / arr[j-1], i, j-1))
        
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]