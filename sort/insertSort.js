/*
 * @Description: 插入排序
 * @Author: leekwe
 * @Date: 2019-06-16 12:44:27
 * @version: 1.0
 * @LastEditors: leekwe
 * @LastEditTime: 2019-06-16 13:33:23
 */
//插入排序（Insertion sort）是一种简单直观且稳定的排序算法。
// 如果有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数，
//但要求插入后此数据序列仍然有序，这个时候就要用到一种新的排序方法——插入排序法,
// 插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
// 从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。
// 是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，
// 但将最后一个元素除外（让数组多一个空间才有插入的位置），而第二部分就只包含这一个元素（即待插入元素）。
// 在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中
const swap = require('../util/help')
/**
 * 它适合已经排序好的数组
 * @param {} arr 
 * @param {*} l 
 * @param {*} h 
 */
const insertSort = (arr, l, h) => {
    for (let i = l; i <= h; i++) {
        // 这层遍历相当于将牌往前面挪
        for (let j = i; j > 0; j--) {
            if (arr[j] < arr[j - 1]) {
                swap(arr, j, j - 1);
            }
        }
    }
    return arr;
}
module.exports = insertSort;
if (require.main === module) {
    let arr = require('../data.json');
    quickStart(arr, 0, arr.length - 1);
    console.log(arr)
}
