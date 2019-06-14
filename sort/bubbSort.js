/*
 * @Author: leekwe 
 * @Date: 2019-06-14 17:53:20 
 * @Last Modified by: leekwe
 * @Last Modified time: 2019-06-14 18:47:00
 */
// 冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。
// 它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果他们的顺序（如从大到小、首字母从A到Z）错误就把他们交换过来。
// 走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成
const swap = require('../util/help');
const bubbSort = (arr, low, high) => {
  for (let i = low; i < high; i++) {
    for (let j = low ; j < high - i; j++) {
      if (arr[j] > arr[j+1]) {
        swap(arr, j, j+1);
      }
    }
  }
  return arr;
};
module.exports = bubbSort;
if (require.main === module) {
  let arr = require('../data.json');
  console.log(bubbSort(arr, 0, arr.length - 1))
}