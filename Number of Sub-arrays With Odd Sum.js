// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/?envType=daily-question&envId=2026-11-15
// Number of Sub-arrays With Odd Sum

/**
 * @param {number[]} arr
 * @return {number}
 */
var numOfSubarrays = function(arr) {
    
    const mod = 10 ** 9 + 7;

    let even = 1;
    let odd = 0;
    let prefix = 0;
    let ans = 0;

    for (const num of arr) {
        prefix = (prefix + num) % 2;

        if (prefix === 0) {
            ans = (ans + odd) % mod;
            even++;
        } else {
            ans = (ans + even) % mod;
            odd++;
        }
    }

    return ans;

};