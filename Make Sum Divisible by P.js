// https://leetcode.com/problems/make-sum-divisible-by-p/submissions/1843530239/?envType=daily-question&envId=2025-11-30
// Make Sum Divisible by P

/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minSubarray = function(nums, p) {
    
    let totalSum = 0;
    
    for (const num of nums) {
        totalSum = (totalSum + num) % p;
    }
    
    const targetRemainder = totalSum;
    
    if (targetRemainder === 0) return 0;

    const modMap = new Map();
    modMap.set(0, -1);
    
    let currentSum = 0;
    let minLen = nums.length;
    
    for (let i = 0; i < nums.length; i++) {
        currentSum = (currentSum + nums[i]) % p;
        
        const needed = (currentSum - targetRemainder + p) % p;
        
        if (modMap.has(needed)) {
            const prevIndex = modMap.get(needed);
            minLen = Math.min(minLen, i - prevIndex);
        }
        
        modMap.set(currentSum, i);
    }
    
    return minLen < nums.length ? minLen : -1;
};