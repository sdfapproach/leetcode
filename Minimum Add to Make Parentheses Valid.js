// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/?envType=daily-question&envId=2026-10-06
// Minimum Add to Make Parentheses Valid

/**
 * @param {string} s
 * @return {number}
 */
var minAddToMakeValid = function(s) {
    const stack = [];
    let top = -1;

    for (const c of s) {
        if (c === "(") {
            stack.push(c);
            top++;
        } else if (c === ")") {
            if (top > -1 && stack[top] === "(") {
                stack.pop();
                top--;
            } else {
                stack.push(c);
                top++;
            }
        }
    }

    return stack.length;
};