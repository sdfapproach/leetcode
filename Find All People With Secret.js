// https://leetcode.com/problems/find-all-people-with-secret/?envType=daily-question&envId=2025-12-19
// Find All People With Secret

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
var findAllPeople = function(n, meetings, firstPerson) {
    const known = new Set([0, firstPerson]);

        meetings.sort((a, b) => a[2] - b[2]);

        let i = 0;

        while (i < meetings.length) {
            const time = meetings[i][2];

            const currentMeetings = [];
            while (i < meetings.length && meetings[i][2] === time) {
                currentMeetings.push(meetings[i]);
                i++;
            }

            const graph = new Map();
            const involvedPeople = new Set();

            for (const [x, y] of currentMeetings) {
                if (!graph.has(x)) graph.set(x, []);
                if (!graph.has(y)) graph.set(y, []);
                graph.get(x).push(y);
                graph.get(y).push(x);
                involvedPeople.add(x);
                involvedPeople.add(y);
            }

            const queue = [];
            const visitedInThisTime = new Set();

            for (const p of involvedPeople) {
                if (known.has(p)) {
                    queue.push(p);
                    visitedInThisTime.add(p);
                }
            }

            // BFS
            while (queue.length > 0) {
                const curr = queue.shift();
                const neighbors = graph.get(curr) || [];

                for (const neighbor of neighbors) {
                    if (!known.has(neighbor)) {
                        known.add(neighbor);
                        visitedInThisTime.add(neighbor);
                        queue.push(neighbor);
                    } else if (!visitedInThisTime.has(neighbor)) {
                        visitedInThisTime.add(neighbor);
                        queue.push(neighbor);
                    }
                }
            }
        }

        return Array.from(known);
};