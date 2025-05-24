// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/?envType=daily-question&envId=2025-05-23
// Find the Maximum Sum of Node Values

/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number[][]} edges
 * @return {number}
 */
var maximumValueSum = function(nums, k, edges) {

    const t = nums.map(i => (i ^ k) - i);

    t.sort((a, b) => b - a);

    let ans = nums.reduce((sum, num) => sum + num, 0);

    let index = 0;

    while (index + 1 < t.length) {
        const adder = t[index] + t[index + 1];
        if (adder > 0) {
            ans += adder;
        } else {
            break;
        }
        index += 2;
    };

    return ans;

};