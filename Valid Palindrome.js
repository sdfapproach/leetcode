// https://leetcode.com/problems/valid-palindrome/description/
// Valid Palindrome

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {

//    const text = s.toLowerCase().replace(/[^a-z0-9]/g, '');

//    const reversed = text.split('').reverse().join('')

//    return text === reversed;
    const cleanText = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    return cleanText === cleanText.split('').reverse().join('');
};