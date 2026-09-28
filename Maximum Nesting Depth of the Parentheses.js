// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=daily-question&envId=2026-09-28
// Maximum Nesting Depth of the Parentheses

/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {

    let count = 0
    let maximum = 0

    for(const c of s) {
      if(c == "("){
        count++;
        maximum = Math.max(count, maximum);
      }
      else if (c == ")"){
        count--;
    };
    
    }
            
    return maximum


};