// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/?envType=daily-question&envId=2025-06-09
// K-th Smallest in Lexicographical Order

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findKthNumber = function(n, k) {
    
    const count_steps = (curr, n) => {
            let steps = 0
            let first = curr
            let last = curr
            
            while (first <= n) {
                steps += Math.min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            }
            return steps
    }

        let current = 1
        k -= 1
        while (k > 0){
            const steps = count_steps(current, n)
            if (steps <= k){
                current += 1
                k -= steps
            }
            else{
                current *= 10
                k--
            }
        }

        return current
};