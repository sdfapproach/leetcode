// https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2026-05-03
// Rotate String

/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    
    for(let i = 0; i < s.length ; i++) {
        if (s == goal) return true;

        s = s.substr(1, s.length) + s[0];
    }

    return false;

};