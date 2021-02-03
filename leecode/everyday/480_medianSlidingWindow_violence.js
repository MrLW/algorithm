/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var medianSlidingWindow = function (nums, k) {
    let len = nums.length;
    if (nums.length == 0 || k > len) return [];
    let left = 0, right = k;
    let result = [];
    let isOdd = k % 2 == 1
    while (right <= len) {
        // 暴力法 这里可以直接排序 nums.slice(left, right), 不推荐, 经测试内存吃不消
        let windows = nums.slice(left, right).sort((a, b) => a - b)
        if (isOdd) {
            result.push(windows[Math.floor(k / 2)]);
        } else {
            let i = k / 2 - 1;
            result.push((windows[i] + windows[i + 1]) / 2)
        }
        left += 1;
        right += 1
    }
    return result;
};

let nums = [1, 4, 2, 3], k = 4;

const result = medianSlidingWindow(nums, k);
console.info(result);