// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/?envType=daily-question&envId=2026-03-14
// The k-th Lexicographical String of All Happy Strings of Length n

/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getHappyString = function(n, k) {
    const happyStrings = [];

    function backtrack(path) {
        if (path.length === n) {
            happyStrings.push(path);
            return;
        }

        for (const ch of "abc") {
            if (path.length === 0 || path[path.length - 1] !== ch) {
                backtrack(path + ch);
            }
        }
    }

    backtrack("");

    happyStrings.sort();

    return k <= happyStrings.length ? happyStrings[k - 1] : "";
};