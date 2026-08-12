// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/?envType=daily-question&envId=2026-08-12
// Length of Longest Subarray With at Most K Frequency

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxSubarrayLength = function(nums, k) {
    
    let start = 0;
    let maxLength = 0;
    const frequency = new Map();

    for (let end = 0; end < nums.length; end++) {
        frequency.set(
            nums[end],
            (frequency.get(nums[end]) || 0) + 1
        );

        while (frequency.get(nums[end]) > k) {
            frequency.set(
                nums[start],
                frequency.get(nums[start]) - 1
            );
            start++;
        }

        maxLength = Math.max(maxLength, end - start + 1);
    }

    return maxLength;

};