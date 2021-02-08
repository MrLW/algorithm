
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var findNumberIn2DArray = function (matrix, target) {
    if (!matrix[0]) {
        return false;
    }
    let cols = matrix[0].length;
    let rows = matrix.length;
    // 通过规律缩小target所在的范围
    let firstRow, endRow;
    for (let i = 0; i < rows; i++) {
        if (firstRow == undefined && matrix[i][cols - 1] >= target) {
            firstRow = i;
        }
        if (matrix[i][0] > target) {
            endRow = i - 1;
            break;
        }
    }
    if (firstRow == undefined) firstRow = 0;
    if (endRow == undefined) endRow = rows - 1;
    let firstCol, endCol;
    for (let j = 0; j < cols; j++) {
        if (firstCol == undefined && matrix[rows - 1][j] >= target) {
            firstCol = j;
        }
        if (matrix[0][j] > target) {
            endCol = j - 1;
        }
    }
    if (firstCol == undefined) firstCol = 0;
    if (endCol == undefined) endCol = cols - 1;
    for (let i = firstRow; i <= endRow; i++) {
        if (matrix[i][firstCol] > target || matrix[i][endCol] < target) {
            continue;
        }
        let row = matrix[i].slice(firstCol, endCol+1);
        do {
            let midPos = Math.ceil(row.length / 2) - 1;
            if (row[midPos] == target) {
                return true;
            } if (row[midPos] > target) {
                row = row.slice(0, midPos);
            } else {
                row = row.slice(midPos + 1);
            }
        } while (row.length);
    }
    return false;
};

let matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

console.info(findNumberIn2DArray(matrix, 15));