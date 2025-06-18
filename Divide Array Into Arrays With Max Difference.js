// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/?envType=daily-question&envId=2025-06-18
// Divide Array Into Arrays With Max Difference

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[][]}
 */
var divideArray = function(nums, k) {
    
    const n = nums.length;

    if (n % 3 !== 0) {
        return [];
    }

    nums.sort((a, b) => a - b);
    const groups = [];

    for (let i = 0; i < n; i += 3) {
        if (nums[i + 2] - nums[i] > k) {
            return [];
        }
        groups.push([nums[i], nums[i + 1], nums[i + 2]]);
    }

    return groups;
};