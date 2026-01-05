// https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2026-01-05
// Maximum Matrix Sum

/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxMatrixSum = function(matrix) {

    const n = matrix.length;
    let totalSum = 0;
    let minAbsValue = Infinity;
    let negativeCount = 0;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const value = matrix[i][j];
            const absValue = Math.abs(value);

            totalSum += absValue;
            minAbsValue = Math.min(minAbsValue, absValue);

            if (value < 0) {
                negativeCount++;
            }
        }
    }

    if (negativeCount % 2 !== 0) {
        totalSum -= 2 * minAbsValue;
    }

    return totalSum;
};