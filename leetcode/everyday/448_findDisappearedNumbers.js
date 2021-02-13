/**
 * 找到所有数组中消失的数字
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    let len = nums.length;
    for(let i = 0 ; i < len ; i++ ){
       let j = (  Math.abs(nums[i]) - 1) % len;
       if(nums[j] > 0) {
           nums[j] = nums[j] * -1;
       }
    }
    let ret = [];
    for(let i = 0 ; i < nums.length;i++) {
        if(nums[i] > 0) ret.push(i+1);
    }
    return ret;
};


var nums = [4,3,2,7,8,2,3,1];
//          1 2 3 4 5 6 7 8
//          3 1 -1 3 3 -4 -4 -7

// 5 6
console.info(findDisappearedNumbers(nums));