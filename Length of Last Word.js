// https://leetcode.com/problems/length-of-last-word/description/
// 58. Length of Last Word

/**
 * @param {string} s
 * @return {number}
 */
// var lengthOfLastWord = function(s) {
//     let text = s;
//     text = text.trim();
//     text = text.split(" ");

//     return text[text.length-1].length

// };
var lengthOfLastWord = function(s) {
    return s.trim().split(" ")[s.trim().split(" ").length-1].length
};