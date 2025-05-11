// https://leetcode.com/problems/three-consecutive-odds/?envType=daily-question&envId=2025-05-11
// Three Consecutive Odds

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {

    let odd_count = 0;
    
    for(let num of arr) {
        if (num % 2 !== 0) odd_count++
        else odd_count = 0

        if (odd_count === 3) return true;
    };

    return false;

};