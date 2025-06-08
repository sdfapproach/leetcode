// https://leetcode.com/problems/lexicographical-numbers/?envType=daily-question&envId=2025-06-08
// Lexicographical Numbers

/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    
    const result = [];
    let curr = 1;
    
    for (let i = 0; i < n; i++) {
        result.push(curr);
        
        if (curr * 10 <= n) {
            curr *= 10;
        } else {
            if (curr >= n) {
                curr = Math.floor(curr / 10);
            }
            curr += 1;
            while (curr % 10 === 0) {
                curr = Math.floor(curr / 10);
            }
        }
    }
    
    return result;

};