// https://leetcode.com/problems/rotate-image/?envType=daily-question&envId=2026-05-04
// Rotate Image

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {

    const n = matrix.length;
    const newMatrix = [];

    for (let i = 0; i < n; i++) {
        const newList = [];
        for (let j = 0; j < n; j++) {
            const newJ = n - j - 1;
            newList.push(matrix[newJ][i]);
        }
        newMatrix.push(newList);
    }

    for (let i = 0; i < n; i++) {
        matrix[i] = newMatrix[i];
    }
};