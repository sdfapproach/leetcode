// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/?envType=daily-question&envId=2026-11-12
// Longest Strictly Increasing or Strictly Decreasing Subarray

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestMonotonicSubarray = function(nums) {
    
    let inc = 1;
    let dec = 1;
    let ans = nums.length > 0 ? 1 : 0;

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i - 1]) {
            inc++;
            dec = 1;
        } else if (nums[i] < nums[i - 1]) {
            dec++;
            inc = 1;
        } else {
            inc = 1;
            dec = 1;
        }

        ans = Math.max(ans, inc, dec);
    }

    return ans;

};