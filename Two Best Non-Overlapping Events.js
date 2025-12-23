// https://leetcode.com/problems/two-best-non-overlapping-events/?envType=daily-question&envId=2025-12-23
// Two Best Non-Overlapping Events

/**
 * @param {number[][]} events
 * @return {number}
 */
var maxTwoEvents = function(events) {
    events.sort((a, b) => a[1] - b[1]);

    let maxValue = 0;
    const maxSingleEvent = [];
    const endTimes = [];

    for (const [, end, value] of events) {
        maxValue = Math.max(maxValue, value);
        maxSingleEvent.push(maxValue);
        endTimes.push(end);
    }

    let result = 0;

    function bisectRight(arr, target) {
        let left = 0, right = arr.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] <= target) left = mid + 1;
            else right = mid;
        }
        return left;
    }

    for (const [start, , value] of events) {
        const idx = bisectRight(endTimes, start - 1) - 1;

        if (idx >= 0) {
            result = Math.max(result, value + maxSingleEvent[idx]);
        } else {
            result = Math.max(result, value);
        }
    }

    return result;
};