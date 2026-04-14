// https://leetcode.com/problems/minimum-total-distance-traveled/?envType=daily-question&envId=2026-04-14
// Minimum Total Distance Traveled

/**
 * @param {number[]} robot
 * @param {number[][]} factory
 * @return {number}
 */
var minimumTotalDistance = function(robot, factory) {
    robot.sort((a, b) => a - b);
    factory.sort((a, b) => a[0] - b[0]);

    const memo = new Map();

    function assignRobots(currPos, robotIdx) {
        if (robotIdx === robot.length) return 0;

        const key = `${currPos},${robotIdx}`;
        if (memo.has(key)) return memo.get(key);

        let result = Infinity;

        if (currPos + 1 < factory.length) {
            result = assignRobots(currPos + 1, robotIdx);
        }

        let robotsAssigned = 0;
        let currDistance = 0;

        while (
            robotIdx + robotsAssigned < robot.length &&
            robotsAssigned < factory[currPos][1]
        ) {
            const r = robot[robotIdx + robotsAssigned];
            const f = factory[currPos][0];

            currDistance += Math.abs(r - f);
            robotsAssigned++;

            if (currPos + 1 < factory.length) {
                const next = assignRobots(
                    currPos + 1,
                    robotIdx + robotsAssigned
                );
                if (next !== Infinity) {
                    result = Math.min(result, currDistance + next);
                }
            } else {
                if (robotIdx + robotsAssigned === robot.length) {
                    result = Math.min(result, currDistance);
                }
            }
        }

        memo.set(key, result);
        return result;
    }

    return assignRobots(0, 0);
};