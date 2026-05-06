// https://leetcode.com/problems/rotating-the-box/?envType=daily-question&envId=2026-05-06
// Rotating the Box

/**
 * @param {character[][]} boxGrid
 * @return {character[][]}
 */
var rotateTheBox = function(boxGrid) {
    const col = boxGrid.length;
    const row = boxGrid[0].length;

    const rotatedBox = Array.from(
        { length: row },
        () => Array(col).fill('.')
    );

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            rotatedBox[i][j] = boxGrid[col - j - 1][i];
        }
    }

    for (let i = 0; i < col; i++) {

        let topStone = null;

        for (let j = 0; j < row; j++) {

            if (topStone === null && rotatedBox[j][i] === '#') {
                topStone = j;

            } else if (rotatedBox[j][i] === '*') {
                topStone = null;

            } else if (topStone !== null && rotatedBox[j][i] === '.') {

                rotatedBox[topStone][i] = '.';
                rotatedBox[j][i] = '#';

                if (
                    topStone + 1 < row &&
                    rotatedBox[topStone + 1][i] === '#'
                ) {
                    topStone += 1;
                } else {
                    topStone = null;
                }
            }
        }
    }

    return rotatedBox;
};