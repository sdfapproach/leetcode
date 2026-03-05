// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/?envType=daily-question&envId=2026-03-05
// Minimum Changes To Make Alternating Binary String

/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {

    let change1 = 0;
    let change2 = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] !== (i % 2 === 0 ? '1' : '0')) change1++;
        if (s[i] !== (i % 2 === 0 ? '0' : '1')) change2++;
    }

    return Math.min(change1, change2);

};