// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/?envType=daily-question&envId=2026-06-30
// Number of Substrings Containing All Three Characters

/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    
    const n = s.length;
    const count = [0, 0, 0];
    let left = 0;
    let res = 0;

    for (let right = 0; right < n; right++) {
        count[s.charCodeAt(right) - 'a'.charCodeAt(0)]++;

        while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
            res += (n - right);
            count[s.charCodeAt(left) - 'a'.charCodeAt(0)]--;
            left++;
        }
    }

    return res;

};