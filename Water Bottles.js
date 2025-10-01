// https://leetcode.com/problems/water-bottles/?envType=daily-question&envId=2025-10-01
// Water Bottles

/**
 * @param {number} numBottles
 * @param {number} numExchange
 * @return {number}
 */
var numWaterBottles = function(numBottles, numExchange) {
    return numBottles + Math.floor((numBottles - 1) / (numExchange - 1));
};