# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/?envType=daily-question&envId=2024-05-30
# Count Triplets That Can Form Two Arrays of Equal XOR

class Solution:
    def countTriplets(self, arr: List[int]) -> int:

        prefix = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]

        count = 0
        xor_count = defaultdict(int)
        xor_total = defaultdict(int)
        
        for j in range(len(arr)):
            if prefix[j + 1] in xor_count:
                count += xor_count[prefix[j + 1]] * j - xor_total[prefix[j + 1]]
            
            xor_count[prefix[j]] += 1
            xor_total[prefix[j]] += j
        
        return count