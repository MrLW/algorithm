/**
 * 数组拆分 I
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    let result = 0;
    nums.sort((a, b) => a - b).forEach((v, i)=>{ 
        result += i % 2 == 0 ? v : 0 
    })
    return result
};
const nums = [6,2,6,5,1,2]
// 1 2 2 5 6 6 
// 1 2 6
console.log(arrayPairSum(nums));