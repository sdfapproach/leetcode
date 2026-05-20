// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/?envType=daily-question&envId=2026-05-20
// Find the Prefix Common Array of Two Arrays

/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var findThePrefixCommonArray = function(A, B) {

    const n = A.length;

    const seenInA = new Set();
    const seenInB = new Set();

    const prefixCommon = [];

    for (let i = 0; i < n; i++) {
        seenInA.add(A[i]);
        seenInB.add(B[i]);

        let commonCount = 0;

        for (const num of seenInA) {
            if (seenInB.has(num)) {
                commonCount++;
            }
        }

        prefixCommon.push(commonCount);
    }

    return prefixCommon;
};