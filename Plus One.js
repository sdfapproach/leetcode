// https://leetcode.com/problems/plus-one/description/
// 66. Plus One

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {

    let carry = true;
    let idx = digits.length - 1;

    while (carry){
        const sum = digits[idx] + 1;

        if(sum < 10) {
            digits[idx] = sum;
            carry = false;
        }
        else{
            digits[idx] = 0;
            if(idx === 0 ) {
                digits.unshift(1);
                carry = false;
            }
        }
        idx--;
    }

    return digits

};