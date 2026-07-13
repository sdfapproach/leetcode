// https://leetcode.com/problems/sequential-digits/?envType=daily-question&envId=2026-07-13
// Sequential Digits

/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    
    const seqDigits = "123456789";
    const result = [];

    const minLen = String(low).length;
    const maxLen = String(high).length;

    for (let length = minLen; length <= maxLen; length++) {
        for (let start = 0; start <= 9 - length; start++) {
            const num = Number(seqDigits.slice(start, start + length));

            if (num >= low && num <= high) {
                result.push(num);
            }
        }
    }

    return result;

};