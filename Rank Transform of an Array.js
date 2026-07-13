// https://leetcode.com/problems/rank-transform-of-an-array/?envType=daily-question&envId=2026-07-12
// Rank Transform of an Array

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    
    const sorted = [...new Set(arr)].sort((a, b) => a - b);

    const rank = new Map();

    for (let i = 0; i < sorted.length; i++) {
        rank.set(sorted[i], i + 1);
    }

    return arr.map(num => rank.get(num));

};