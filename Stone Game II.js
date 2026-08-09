// https://leetcode.com/problems/stone-game-ii/?envType=daily-question&envId=2026-08-09
// Stone Game II

/**
 * @param {number[]} piles
 * @return {number}
 */
var stoneGameII = function(piles) {
    
    const n = piles.length;

    const memo = Array.from(
        { length: n + 1 },
        () => Array.from(
            { length: n + 1 },
            () => [-1, -1]
        )
    );

    function solve(i, m, t) {
        if (i >= n) return 0;

        if (memo[i][m][t] !== -1) {
            return memo[i][m][t];
        }

        let stones = 0;
        let res = t === 0 ? -1 : Infinity;

        for (let x = 1; x <= 2 * m; x++) {
            if (i + x - 1 >= n) break;

            stones += piles[i + x - 1];

            if (t === 0) {
                res = Math.max(
                    res,
                    stones + solve(i + x, Math.max(x, m), 1)
                );
            } else {
                res = Math.min(
                    res,
                    solve(i + x, Math.max(x, m), 0)
                );
            }
        }

        memo[i][m][t] = res;
        return res;
    }

    return solve(0, 1, 0);

};