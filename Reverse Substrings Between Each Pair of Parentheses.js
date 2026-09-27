// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/?envType=daily-question&envId=2026-09-27
// Reverse Substrings Between Each Pair of Parentheses

/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function(s) {
    
    const stack = [];

    for (const char of s) {
        if (char === ")") {
            const subString = [];

            while (stack.length > 0) {
                if (stack[stack.length - 1] === "(") {
                    stack.pop();
                    break;
                }

                subString.push(stack.pop());
            }

            stack.push(...subString);
        } else {
            stack.push(char);
        }
    }

    return stack.join("");
};