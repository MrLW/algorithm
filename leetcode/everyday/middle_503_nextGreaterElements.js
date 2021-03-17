/**
 * 下一个更大元素 II
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function (nums) {
    const n = nums.length;
    const ret = new Array(n).fill(-1);
    const stk = [];
    for (let i = 0; i < n * 2 - 1; i++) {
        while (stk.length && nums[stk[stk.length - 1]] < nums[i % n]) {
            ret[stk[stk.length - 1]] = nums[i % n];
            stk.pop();
        }
        stk.push(i % n);
    }
    return ret;

    // 暴力法
    // let result = [];
    // for (let i = 0; i < nums.length - 1; i++) {
    //     for (var j = i; j < i + nums.length; j++) {
    //         if (nums[j % nums.length] > nums[i]) {
    //             result.push(nums[j % nums.length]);
    //             break;
    //         }
    //     }
    //     if (j - i == nums.length) {
    //         result.push(-1);
    //     }
    // }
    // // 最后一个元素
    // for (var i = 0; i < nums.length - 1; i++) {
    //     if (nums[i] > nums[nums.length - 1]) {
    //         result.push(nums[i]);
    //         break;
    //     }
    // }
    // if (i == nums.length - 1) {
    //     result.push(-1);
    // }
    // return result;
};
// const nums = [5, 4, 3, 2, 1];
//              [-1,-1,-1,-1];
const nums = [4, 2, 1, 3];// =====> -1 3 3 4
console.info(nextGreaterElements(nums));