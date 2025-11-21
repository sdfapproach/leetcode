// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/?envType=daily-question&envId=2025-11-21
// Unique Length-3 Palindromic Subsequences

/**
 * @param {string} s
 * @return {number}
 */
var countPalindromicSubsequence = function(s) {
    const n = s.length;
    const first = Array(26).fill(Infinity);
    const last = Array(26).fill(-1);
    
    for (let i = 0; i < n; i++) {
        const idx = s.charCodeAt(i) - 97;
        first[idx] = Math.min(first[idx], i);
        last[idx] = Math.max(last[idx], i);
    }

    let ans = 0;

    for (let c = 0; c < 26; c++) {
        if (first[c] < last[c]) { 
            const used = new Set();
            for (let i = first[c] + 1; i < last[c]; i++) {
                used.add(s[i]);
            }
            ans += used.size;
        }
    }

    return ans;
};