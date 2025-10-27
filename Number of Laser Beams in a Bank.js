// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/?envType=daily-question&envId=2025-10-27
// Number of Laser Beams in a Bank

/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function(bank) {
    
    let prevDevices = 0;
    let totalBeams = 0;

    for (const row of bank) {
        const devices = [...row].filter(c => c === '1').length;
        if (devices > 0) {
        totalBeams += prevDevices * devices;
        prevDevices = devices;
        }
    }

    return totalBeams;

};