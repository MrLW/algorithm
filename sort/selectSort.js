/*
 * @Author: leekwe 
 * @Date: 2019-06-14 15:43:51 
 * @Last Modified by: leekwe
 * @Last Modified time: 2019-06-14 18:28:55
 */
//选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，
//存放在序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
//以此类推，直到全部待排序的数据元素排完。 选择排序是不稳定的排序方法。
const swap = require('../util/help');
const selectSort = (arr,low,high) => {
  for (let i = low; i < high; i++) {
    for (let j = i; j < arr.length; j++) {
      if (arr[i] > arr[j])
        swap(arr, i, j);
    }
  }
  return arr;
}

module.exports = selectSort ;
if(require.main === module){
  let arr = require('../data.json');
  console.log(selectSort(arr,0,arr.length-1));
}