/**
 * 下一个更大元素 II
 * @param {number[]} nums
 * @return {number[]}
 */
var nextGreaterElements = function (nums) {
    // 暴力法
    let result = [];
    for (let i = 0; i < nums.length - 1; i++) {
        for (var j = i; j < i + nums.length; j++) {
            if (nums[j % nums.length] > nums[i]) {
                result.push(nums[j % nums.length]);
                break;
            }
        }
        if (j - i == nums.length) {
            result.push(-1);
        }
    }
    // 最后一个元素
    for (var i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[nums.length - 1]) {
            result.push(nums[i]);
            break;
        }
    }
    if (i == nums.length - 1) {
        result.push(-1);
    }
    return result;
};
const nums = [5, 4, 3, 2, 1];
console.info(nextGreaterElements(nums));