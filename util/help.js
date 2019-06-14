/*
 * @Author: leekwe 
 * @Date: 2019-06-14 15:59:28 
 * @Last Modified by: leekwe
 * @Last Modified time: 2019-06-14 16:00:18
 */
const swap = (arr, i, j) => {
  let temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}
module.exports = swap ;