// https://leetcode.com/problems/count-servers-that-communicate/?envType=daily-question&envId=2026-11-08
// Count Servers that Communicate

/**
 * @param {number[][]} grid
 * @return {number}
 */
var countServers = function(grid) {
    
    const m = grid.length;
    const n = grid[0].length;

    const rowCount = new Array(m).fill(0);
    const colCount = new Array(n).fill(0);

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                rowCount[i]++;
                colCount[j]++;
            }
        }
    }

    let count = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (
                grid[i][j] === 1 &&
                (rowCount[i] > 1 || colCount[j] > 1)
            ) {
                count++;
            }
        }
    }

    return count;
};