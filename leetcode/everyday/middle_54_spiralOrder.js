/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  // 1,2,3,4
  // 1: 向下
  // 2: 向左
  // 3:向上
  // 4: 向右

  let result = [];
  let startRow = 0,
    endRow = matrix.length,
    startCol = 0,
    endCol = matrix[0].length;
  while (startRow < endRow && startCol < endCol) {
    // 第一行
    for (let i = startCol; i < endCol && startCol != endCol; i++) {
      result.push(matrix[startRow][i]);
    }
    // 最后一列
    for (let i = startRow + 1; i < endRow && startRow != endRow; i++) {
      result.push(matrix[i][endCol - 1]);
    }
    // 最后一行
    for (let i = endCol - 2; i >= startCol && endRow - 1 != startRow; i--) {
      result.push(matrix[endRow - 1][i]);
    }
    // 第一列
    for (let i = endRow - 2; i > startRow && startCol != endCol - 1; i--) {
      result.push(matrix[i][startCol]);
    }
    endRow = endRow - 1;
    endCol = endCol - 1;
    startRow = startRow + 1;
    startCol = startCol + 1;
  }
  return result;
};

const matrix = [
  //   [1, 2, 3],
  //   [4, 5, 6],
  //   [7, 8, 9],
  //   [10, 11, 12],
  //   [1, 2, 3, 'a'],
  //   [4, 5, 6, 'b'],
  //   [7, 8, 9, 'c'],
  //   [10, 11, 12, 'd'],
  [7],
  [9],
  [6],
];

console.info(spiralOrder(matrix));
