/**
 * 重塑矩阵
 * @param {number[][]} nums
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function (nums, r, c) {
  let sr = nums.length,
    sc = nums[0].length;
  let total = r * c;
  if (total != sr * sc) {
    return nums;
  }
  let result = [],
    temp = [],
    x = 0;
  for (let i = 0; i < sr; i++) {
    for (let j = 0; j < sc; j++) {
      temp[x++] = nums[i][j];
    }
  }
  for (let i = 0; i < r; i++) {
    let item = [];
    for (let j = 0; j < c; j++) {
      item[j] = temp[i * c+ j];
    }
    result.push(item);
  }
  return result;
};

// [[1,2],[3,4]]
// 4
// 1
const nums = [
    [1, 2],
    [3, 4],
  ],
  r = 4,
  c = 1;
console.info(matrixReshape(nums, r, c));
