/**单调数列
 * @param {number[]} A
 * @return {boolean}
 */
var isMonotonic = function (A) {
  let i = 0,
    flag;
  while (i < A.length - 1) {
    if (A[i] > A[i + 1]) {
      // 递减
      flag = 0;
      break;
    } else if (A[i] < A[i + 1]) {
      // 递增
      flag = 1;
      break;
    }
    i++;
  }

  while (i < A.length - 1) {
    if (flag && A[i] > A[i + 1]) {
      return false;
    } else if (!flag && A[i] < A[i + 1]) {
      return false;
    }
    i++;
  }
  return true;
};

let A = [1, 3, 2];
console.info(isMonotonic(A));
