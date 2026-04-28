// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/?envType=daily-question&envId=2026-04-28
//  Minimum Operations to Make a Uni-Value Grid

/**
 * @param {number[][]} grid
 * @param {number} x
 * @return {number}
 */
var minOperations = function(grid, x) {
    const arr = [];
    for (const row of grid) {
        for (const num of row) {
            arr.push(num);
        }
    }

    const mod = arr[0] % x;

    for (const num of arr) {
        if (num % x !== mod) {
            return -1;
        }
    }

    arr.sort((a, b) => a - b);

    const median = arr[Math.floor(arr.length / 2)];

    let ops = 0;
    for (const num of arr) {
        ops += Math.floor(Math.abs(num - median) / x);
    }

    return ops;
};