// https://leetcode.com/problems/delete-characters-to-make-fancy-string/?envType=daily-question&envId=2025-07-21
// Delete Characters to Make Fancy String

/**
 * @param {string} s
 * @return {string}
 */
var makeFancyString = function(s) {
    
    let char = ""
    let count = 1
    let fancy_string = ""

    for(const c of s){
        if( c == char){
            count += 1
            if (count < 3) fancy_string += c
        }
        else{
            count = 1
            char = c
            fancy_string += c
        }
    }
    return fancy_string

};