// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
// Two Sum II - Input Array Is Sorted

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    for(let i=0; i<numbers.length;i++){
        for(let j=i+1; j<numbers.length;j++){
            if(numbers[i] + numbers[j] === target) {
                return [i+1, j+1];
            };
        };
    };
};