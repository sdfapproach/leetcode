// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/?envType=daily-question&envId=2026-05-23
// Check if Array Is Sorted and Rotated

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var check = function(nums) {
    
    const n = nums.length;
    let dropCount = 0;

    for (let i = 0; i < n; i++) {
        if (nums[i] > nums[(i + 1) % n]) {
            dropCount++;
        }
    }

    return dropCount <= 1;
};