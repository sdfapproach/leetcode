// https://leetcode.com/problems/walking-robot-simulation/?envType=daily-question&envId=2026-04-06
// Walking Robot Simulation

/**
 * @param {number[]} commands
 * @param {number[][]} obstacles
 * @return {number}
 */
var robotSim = function(commands, obstacles) {
    let x = 0, y = 0;
    let heading = 0;
    let longest = 0;

    const obstacleSet = new Set(
        obstacles.map(([ox, oy]) => `${ox},${oy}`)
    );

    const direction = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0]
    ];

    for (const move of commands) {
        if (move === -1) {
            heading = (heading + 1) % 4;
        } else if (move === -2) {
            heading = (heading + 3) % 4;
        } else {
            for (let i = 0; i < move; i++) {
                const nextX = x + direction[heading][0];
                const nextY = y + direction[heading][1];

                if (obstacleSet.has(`${nextX},${nextY}`)) {
                    break;
                }

                x = nextX;
                y = nextY;
            }

            longest = Math.max(longest, x * x + y * y);
        }
    }

    return longest;
};