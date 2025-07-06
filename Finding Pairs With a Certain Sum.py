# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/description/?envType=daily-question&envId=2025-07-06
# Finding Pairs With a Certain Sum

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:

        old = self.nums2[index]
        self.freq2[old] -= 1

        if self.freq2[old] == 0:
            del self.freq2[old]
        
        new = old + val

        self.nums2[index] = new
        self.freq2[new] += 1

    def count(self, tot: int) -> int:
        ans = 0

        for x, cnt_x in self.freq1.items():
            need = tot - x
            ans += cnt_x * self.freq2.get(need, 0)

        return ans



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)