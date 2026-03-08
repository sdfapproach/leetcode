// https://leetcode.com/problems/find-unique-binary-string/?envType=daily-question&envId=2026-03-08
// Find Unique Binary String

/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    
        const n = nums.length;
        const answer = [];

        for (let i = 0; i < n; i++) {
            if (nums[i][i] === '0') {
                answer.push('1');
            } else {
                answer.push('0');
            }
        }

        return answer.join("");
};