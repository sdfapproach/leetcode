// https://leetcode.com/problems/compare-version-numbers/?envType=daily-question&envId=2025-09-23
// Compare Version Numbers

/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    const v1 = version1.split('.').map(num => parseInt(num, 10));
    const v2 = version2.split('.').map(num => parseInt(num, 10));

    const n = Math.max(v1.length, v2.length);

    for (let i = 0; i < n; i++) {
        const rev1 = i < v1.length ? v1[i] : 0;
        const rev2 = i < v2.length ? v2[i] : 0;

        if (rev1 < rev2) return -1;
        if (rev1 > rev2) return 1;
    }
    return 0;
};