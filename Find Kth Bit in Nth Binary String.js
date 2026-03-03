// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=daily-question&envId=2026-03-03
// Find Kth Bit in Nth Binary String

/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    if (n === 1) return "0";

    const length = (1 << n) - 1;
    const mid = (length + 1) >> 1;

    if (k === mid) return "1";

    if (k < mid) {
        return findKthBit(n - 1, k);
    }

    const mirrored = length - k + 1;
    const bit = findKthBit(n - 1, mirrored);

    return bit === "0" ? "1" : "0";
    };