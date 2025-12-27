// https://leetcode.com/problems/meeting-rooms-iii/?envType=daily-question&envId=2025-12-27
// Meeting Rooms III

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @return {number}
 */

var mostBooked = function(n, meetings) {
    meetings.sort((a, b) => a[0] - b[0]);

    const idle = [];

    for (let i = 0; i < n; i++) idle.push(i);
    idle.sort((a, b) => a - b);

    const busy = [];

    const cnt = Array(n).fill(0);

    const pushBusy = (item) => {
        busy.push(item);
        busy.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    };

    const pushIdle = (room) => {
        idle.push(room);
        idle.sort((a, b) => a - b);
    };

    for (const [s, e] of meetings) {
        while (busy.length && busy[0][0] <= s) {
            const [, room] = busy.shift();
            pushIdle(room);
        }

        if (idle.length) {
            const room = idle.shift();
            cnt[room]++;
            pushBusy([e, room]);
        } else {
            const [endTime, room] = busy.shift();
            cnt[room]++;
            pushBusy([endTime + (e - s), room]);
        }
    }

    let ans = 0;

    for (let i = 1; i < n; i++) {
        if (cnt[i] > cnt[ans]) ans = i;
    }

    return ans;
};