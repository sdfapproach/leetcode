// https://leetcode.com/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2025-09-22
// Count Elements With Maximum Frequency

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    const freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    let maxf = 0;
    for (const count of freq.values()) {
        if (count > maxf) maxf = count;
    }

    let total = 0;
    for (const count of freq.values()) {
        if (count === maxf) total += count;
    }

    return total;
};