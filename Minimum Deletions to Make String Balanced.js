// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/?envType=daily-question&envId=2026-02-07
// Minimum Deletions to Make String Balanced

/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function(s) {

    const n = s.length;

    const aPref = new Array(n + 1).fill(0);
    
    for (let i = 0; i < n; ++i) {
        aPref[i + 1] = aPref[i] + (s[i] === 'a' ? 1 : 0);
    }

    const bSuf = new Array(n + 1).fill(0);

    for (let i = n - 1; i >= 0; --i) {
        bSuf[i] = bSuf[i + 1] + (s[i] === 'b' ? 1 : 0);
    }

    let best = 0;

    for (let i = 0; i <= n; ++i) {
        const cur = aPref[i] + bSuf[i];
        if (cur > best) best = cur;
    }

    return deletions = n - best;
};