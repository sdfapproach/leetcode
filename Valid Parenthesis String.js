// https://leetcode.com/problems/valid-parenthesis-string/?envType=daily-question&envId=2026-10-04
// Valid Parenthesis String

/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
    const leftStack = [];
    const starStack = [];

    for (let i = 0; i < s.length; i++) {
        const ch = s[i];

        if (ch === '(') {
            leftStack.push(i);
        } else if (ch === '*') {
            starStack.push(i);
        } else if (ch === ')') {
            if (leftStack.length > 0) {
                leftStack.pop();
            } else if (starStack.length > 0) {
                starStack.pop();
            } else {
                return false;
            }
        }
    }

    while (leftStack.length > 0 && starStack.length > 0) {
        if (
            leftStack[leftStack.length - 1] <
            starStack[starStack.length - 1]
        ) {
            leftStack.pop();
            starStack.pop();
        } else {
            return false;
        }
    }

    return leftStack.length === 0;
};