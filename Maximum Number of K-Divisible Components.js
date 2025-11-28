// https://leetcode.com/problems/maximum-number-of-k-divisible-components/?envType=daily-question&envId=2025-11-28
// Maximum Number of K-Divisible Components

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} values
 * @param {number} k
 * @return {number}
 */
var maxKDivisibleComponents = function(n, edges, values, k) {
    
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }

    let components = 0;

    const dfs = (node, parent) => {
        let sum = values[node];

        for (const nxt of g[node]) {
            if (nxt === parent) continue;
            sum += dfs(nxt, node);
        }

        if (sum % k === 0) {
            components++;
            return 0;
        }

        return sum;
    };

    dfs(0, -1);

    return components;
};