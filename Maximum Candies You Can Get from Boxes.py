# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/?envType=daily-question&envId=2025-06-03
# Maximum Candies You Can Get from Boxes

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        n = len(status)
        haveKey = [False] * n
        visited = [False] * n
        inOwnedClosed = [False] * n

        q = deque(initialBoxes)

        total_candies = 0

        while q:
            b = q.popleft()
            if visited[b]:
                continue
            if status[b] == 1 or haveKey[b]:
                visited[b] = True
                total_candies += candies[b]
                for k in keys[b]:
                    if not haveKey[k]:
                        haveKey[k] = True
                        if inOwnedClosed[k]:
                            q.append(k)
                            inOwnedClosed[k] = False
                for nb in containedBoxes[b]:
                    if not visited[nb]:
                        q.append(nb)
            else:
                inOwnedClosed[b] = True

        return total_candies