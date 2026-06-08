// https://leetcode.com/problems/partition-array-according-to-given-pivot/?envType=daily-question&envId=2026-06-08
// Partition Array According to Given Pivot

/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    
    const left = nums.filter(x => x < pivot);
    const middle = nums.filter(x => x === pivot);
    const right = nums.filter(x => x > pivot);

    return [...left, ...middle, ...right];

};