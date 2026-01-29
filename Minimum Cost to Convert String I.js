// https://leetcode.com/problems/minimum-cost-to-convert-string-i/?envType=daily-question&envId=2026-01-29
// Minimum Cost to Convert String I

/**
 * @param {string} source
 * @param {string} target
 * @param {character[]} original
 * @param {character[]} changed
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(source, target, original, changed, cost) {
    const ALPHABET_SIZE = 26;
    const INF = Infinity;
    
    const dist = Array.from({ length: ALPHABET_SIZE }, () => 
        new Array(ALPHABET_SIZE).fill(INF)
    );
    
    for (let i = 0; i < ALPHABET_SIZE; i++) {
        dist[i][i] = 0;
    }
    
    for (let i = 0; i < original.length; i++) {
        const from = original[i].charCodeAt(0) - 97; // 'a'는 97
        const to = changed[i].charCodeAt(0) - 97;
        
        dist[from][to] = Math.min(dist[from][to], cost[i]);
    }
    
    for (let k = 0; k < ALPHABET_SIZE; k++) {
        for (let i = 0; i < ALPHABET_SIZE; i++) {
            for (let j = 0; j < ALPHABET_SIZE; j++) {
                if (dist[i][k] !== INF && dist[k][j] !== INF) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    let totalCost = 0;
    
    for (let i = 0; i < source.length; i++) {
        const u = source.charCodeAt(i) - 97;
        const v = target.charCodeAt(i) - 97;
        
        if (dist[u][v] === INF) {
            return -1;
        }
        
        totalCost += dist[u][v];
    }
    
    return totalCost;
};