// https://leetcode.com/problems/robot-collisions/?envType=daily-question&envId=2026-04-01
// Robot Collisions

/**
 * @param {number[]} positions
 * @param {number[]} healths
 * @param {string} directions
 * @return {number[]}
 */
var survivedRobotsHealths = function(positions, healths, directions) {
    const n = positions.length;

    const robots = positions
        .map((pos, i) => [pos, healths[i], directions[i], i])
        .sort((a, b) => a[0] - b[0]);

    const stack = [];

    for (let [pos, health, dir, idx] of robots) {

        if (dir === 'R') {
            stack.push([pos, health, dir, idx]);
        } else {
            while (stack.length && stack[stack.length - 1][2] === 'R') {

                let [r_pos, r_health, r_dir, r_idx] = stack.pop();

                if (r_health > health) {
                    r_health -= 1;
                    stack.push([r_pos, r_health, r_dir, r_idx]);
                    health = 0;
                    break;
                } else if (r_health < health) {
                    health -= 1;
                } else {
                    health = 0;
                    break;
                }
            }

            if (health > 0) {
                stack.push([pos, health, dir, idx]);
            }
        }
    }

    const result = new Array(n).fill(0);

    for (let [pos, health, dir, idx] of stack) {
        result[idx] = health;
    }

    return result.filter(h => h > 0);
};