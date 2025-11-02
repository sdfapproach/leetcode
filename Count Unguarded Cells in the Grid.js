// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/?envType=daily-question&envId=2025-11-02
// Count Unguarded Cells in the Grid

/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} guards
 * @param {number[][]} walls
 * @return {number}
 */
var countUnguarded = function(m, n, guards, walls) {
    
    const grid = Array.from({ length: m }, () => Array(n).fill(0));

    for (const [r, c] of guards) grid[r][c] = 1;
    for (const [r, c] of walls) grid[r][c] = 2;

    const dirs = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ];

    for (const [gr, gc] of guards) {
        for (const [dr, dc] of dirs) {
        let r = gr + dr, c = gc + dc;
        while (r >= 0 && r < m && c >= 0 && c < n) {
            if (grid[r][c] === 2 || grid[r][c] === 1) break;
            if (grid[r][c] === 0) grid[r][c] = 3;
            r += dr;
            c += dc;
        }
        }
    }

    let unguarded = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
        if (grid[i][j] === 0) unguarded++;
        }
    }
    return unguarded;

};