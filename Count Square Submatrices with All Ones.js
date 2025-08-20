// https://leetcode.com/problems/count-square-submatrices-with-all-ones/?envType=daily-question&envId=2025-08-20
// Count Square Submatrices with All Ones

/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function(matrix) {
    const m = matrix.length, n = m ? matrix[0].length : 0;
    if (!m || !n) return 0;
    const dp = Array.from({ length: m }, () => Array(n).fill(0));
    let ans = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
        if (matrix[i][j] === 1) {
            if (i === 0 || j === 0) {
            dp[i][j] = 1;
            } else {
            dp[i][j] = 1 + Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]);
            }
            ans += dp[i][j];
        }
        }
    }
    return ans;
};