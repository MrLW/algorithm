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
  let result = new Array(r).fill(0).map((item) => new Array(c).fill(0));
  for (let i = 0; i < r * c; i++) {
    result[Math.floor(i / c)][Math.floor(i % c)] =
      nums[Math.floor(i / sc)][Math.floor(i % sc)];
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
