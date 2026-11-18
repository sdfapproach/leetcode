// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/?envType=daily-question&envId=2026-11-18
// Minimum Number of Changes to Make Binary String Beautiful

/**
 * @param {string} s
 * @return {number}
 */
var minChanges = function(s) {
    
        let count = 0;
        const iter = Math.floor((s.length)/2);

        for(let i = 0; i < iter ; i++){
            const idx = i * 2;

            if(s[idx] != s[idx+1]) count ++;
        }


        return count;

};