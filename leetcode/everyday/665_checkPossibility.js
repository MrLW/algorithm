/**
 * type: Easy
 * 思路: 
 *      第i+1和第i元素比较大小, 如果第i个元素大,则 需要修改i/i+1的值让前i+1个元素有序, 
 *      为了让整个数组有序, 则尽量让i和i+1中让较小的元素作为i/i+1,但是有一个前提, 替换i之后保证有序, 即保证 nums[i] >= nums[i-1](考虑好i-1位0的情况)
 *      
 * 
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function (nums) {
    let pos = 0;
    let len = nums.length;
    let count = 0;
    if (nums[0] > nums[1]) {
        count++;
        nums[0] = nums[1];
    }
    while (pos < len) {
        if (nums[pos] > nums[pos + 1]) {
            if (nums[pos + 1] >= nums[pos - 1]) {
                nums[pos] = nums[pos + 1];
            } else {
                nums[pos + 1] = nums[pos]
            }
            count++;
        }
        pos++;
        if (count > 1) {
            return false;
        }
    }
    return true;
};
// 要么 i+1变成i    
// 要么 i 变成 i+1
const nums = [3, 4, 2, 3]
const nums2 = [5, 7, 1, 8]
const nums3 = [1, 2, 8, 6, 7]
const nums4 = [4, 2, 3]
const nums5 = [1, 4, 1, 2]
const result = checkPossibility(nums5);
console.info(result);