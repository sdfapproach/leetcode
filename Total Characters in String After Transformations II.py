# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/?envType=daily-question&envId=2025-05-14
# Total Characters in String After Transformations II

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        SIZE = 26

        def multiply_matrices(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            C = [[0] * SIZE for _ in range(SIZE)]
            for i in range(SIZE):
                for j in range(SIZE):
                    sum_val = 0
                    for k_inner in range(SIZE):
                        sum_val = (sum_val + A[i][k_inner] * B[k_inner][j]) % MOD
                    C[i][j] = sum_val
            return C

        def matrix_power(M: List[List[int]], p: int) -> List[List[int]]:
            res = [[0] * SIZE for _ in range(SIZE)]
            for i in range(SIZE):
                res[i][i] = 1
            
            base = M
            while p > 0:
                if p % 2 == 1:
                    res = multiply_matrices(res, base)
                base = multiply_matrices(base, base)
                p //= 2
            return res

        if t == 0:
            return len(s) % MOD

        T_matrix = [[0] * SIZE for _ in range(SIZE)]

        for r in range(SIZE):
            N_chars_generated = nums[r]
            
            if N_chars_generated == 0:
                continue

            for c_col in range(SIZE): # Target generated character index
                j_base = ((c_col - r - 1 + SIZE) % SIZE) + 1

                if j_base > N_chars_generated:
                    T_matrix[r][c_col] = 0
                else:
                    count = (N_chars_generated - j_base) // SIZE + 1
                    T_matrix[r][c_col] = count % MOD

        Result_Matrix = matrix_power(T_matrix, t)

        L_t_for_each_char = [0] * SIZE
        for i in range(SIZE):
            row_sum = 0
            for j in range(SIZE):
                row_sum = (row_sum + Result_Matrix[i][j]) % MOD
            L_t_for_each_char[i] = row_sum
        
        total_final_length = 0
        for char_from_s in s:
            char_idx = ord(char_from_s) - ord('a')
            total_final_length = (total_final_length + L_t_for_each_char[char_idx]) % MOD
            
        return total_final_length