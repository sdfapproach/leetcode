// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/?envType=daily-question&envId=2026-07-31
// Minimum Number of Pushes to Type Word II

/**
 * @param {string} word
 * @return {number}
 */
var minimumPushes = function(word) {
    
    const frequencyMap = new Map();

    for (const char of word) {
        frequencyMap.set(char, (frequencyMap.get(char) || 0) + 1);
    }

    const frequencies = [...frequencyMap.values()]
        .sort((a, b) => b - a);

    let answer = 0;

    for (let i = 0; i < frequencies.length; i++) {
        const pushes = Math.floor(i / 8) + 1;
        answer += frequencies[i] * pushes;
    }

    return answer;

};