// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/?envType=daily-question&envId=2026-07-27
// Maximum Product of Two Elements in an Array

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {

    let max1 = Math.max(...nums);

    nums.splice(nums.indexOf(max1), 1);

    let max2 = Math.max(...nums);

    return (max1 - 1) * (max2 - 1);

};