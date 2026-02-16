// https://leetcode.com/problems/add-binary/?envType=daily-question&envId=2026-02-15
// Add Binary

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {

    let i = a.length - 1;
    let j = b.length - 1;
    let carry = 0;
    let result = [];

    while (i >= 0 || j >= 0 || carry) {
        let sum = carry;

        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';

        result.push(sum % 2);
        carry = Math.floor(sum / 2);
    }

    return result.reverse().join('');
};