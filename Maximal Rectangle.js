// https://leetcode.com/problems/maximal-rectangle/?envType=daily-question&envId=2026-01-11
// Maximal Rectangle

/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
    if (!matrix || matrix.length === 0) return 0;

    const rows = matrix.length;
    const cols = matrix[0].length;

    const heights = new Array(cols + 1).fill(0);
    let maxArea = 0;

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (matrix[r][c] === '1') {
                heights[c] += 1;
            } else {
                heights[c] = 0;
            }
        }

        const stack = [];
        for (let i = 0; i < heights.length; i++) {
            while (stack.length && heights[i] < heights[stack[stack.length - 1]]) {
                const h = heights[stack.pop()];
                const w = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
                maxArea = Math.max(maxArea, h * w);
            }
            stack.push(i);
        }
    }

    return maxArea;
};