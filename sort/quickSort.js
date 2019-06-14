/*
 * @Author: leekwe 
 * @Date: 2019-06-14 15:56:54 
 * @Last Modified by: leekwe
 * @Last Modified time: 2019-06-14 18:20:06
 */
// 快速排序由C. A. R. Hoare在1960年提出。它的基本思想是：通过一趟排序将要排序的数据分割成独立的两部分，
// 其中一部分的所有数据都比另外一部分的所有数据都要小，然后再按此方法对这两部分数据分别进行快速排序，
// 整个排序过程可以递归进行，以此达到整个数据变成有序序列
const quickStart = (arr, low, high) => {
  let l = low, h = high;
  if (l < h) {
    // 将low作为基准,比arr[low]小的排到左边,比arr[low]大的排到右边
    let k = arr[low];
    // 经过此处while,就是获取新的low、high
    while (l != h) {
      while (l < h && k <= arr[h]) {
        h--;
      }
      arr[l] = arr[h];
      while (l < h && k >= arr[l]) {
        l++;
      }
      arr[h] = arr[l];
    }
    // 此处的l等于h, 就是新的基准,
    arr[h] = k;
    quickStart(arr, low, l - 1);
    quickStart(arr, l + 1, high);
  }
  return arr;
}
module.exports = quickStart;

if (require.main === module) {
  let arr = require('../data.json');
  quickStart(arr, 0, arr.length - 1);
  console.log(arr)
}
