// https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2025-12-25
// Maximize Happiness of Selected Children

/**
 * @param {number[]} happiness
 * @param {number} k
 * @return {number}
 */
var maximumHappinessSum = function(happiness, k) {
    happiness.sort((a, b) => b - a);

    let total = 0;

    for (let i = 0; i < k; i++) {
        const gain = happiness[i] - i;
        if (gain <= 0) break;
        total += gain;
    }

    return total;
};