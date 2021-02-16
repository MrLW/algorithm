/**
 * 最大连续1的个数
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let maxCount = 0, lastMaxCount = 0, i = 0;
    while (i < nums.length) {
       if(nums[i++]){
           maxCount++;
       }else {
           lastMaxCount = Math.max(maxCount, lastMaxCount);
           maxCount = 0;
       }
    }
    return Math.max(maxCount, lastMaxCount);
};
const nums= [1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1]
console.info(findMaxConsecutiveOnes(nums));