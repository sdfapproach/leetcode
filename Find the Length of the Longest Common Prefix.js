// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/?envType=daily-question&envId=2026-05-21
// Find the Length of the Longest Common Prefix

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var longestCommonPrefix = function(arr1, arr2) {
    
    function getPrefixes(num) {
        const strNum = String(num);
        const prefixes = new Set();

        for (let i = 1; i <= strNum.length; i++) {
            prefixes.add(strNum.slice(0, i));
        }

        return prefixes;
    }

    const prefixSet = new Set();

    for (const num1 of arr1) {
        const prefixes = getPrefixes(num1);

        for (const p of prefixes) {
            prefixSet.add(p);
        }
    }

    let maxLength = 0;

    for (const num2 of arr2) {
        const strNum2 = String(num2);

        for (let i = 1; i <= strNum2.length; i++) {
            const prefix = strNum2.slice(0, i);

            if (prefixSet.has(prefix)) {
                maxLength = Math.max(maxLength, prefix.length);
            }
        }
    }

    return maxLength;
};