// https://leetcode.com/problems/array-reduce-transformation/
// Array Reduce Transformation

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    
    return nums.reduce((accum, num) => fn(accum, num), init);
};