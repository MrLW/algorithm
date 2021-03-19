/**
 * 乘积最大子数组
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
    // 1. 当 nums[i] >= 0:
    //      1.1: 若 iMax[i-1] > 0 , 则 iMax[i] = iMax[i-1] * nums[i]
    //      1.2: 若 IMAX[i-1] < 0,  则 iMax[i] = nums[i]
    // 2. 当 nums[i] < 0:
    //      2.1: 若 iMax[i-1] < 0, 则 iMax[i] = iMin[i-1] * nums[i]
    //      2.2: 若 iMax[i-1] > 0, 则 iMax[i] = nums[i]
    if (nums.length == 0) {
        return 0;
    }
    let max = nums[0], iMax = nums[0], iMin = nums[0];
    for (let i = 1; i < nums.length; i++) {
        var preMax = iMax;
        iMax = Math.max(iMin * nums[i], Math.max(nums[i] * iMax, nums[i]));
        iMin = Math.min(iMin * nums[i], Math.min(nums[i] * preMax, nums[i]));
        max = Math.max(max, iMax);
    }
    return max;
}


/**
 * 两层内循环超时,
 * 貌似这个写法没有用到dp, 还多了一个for 傻了
 * @param {*} nums 
 * @returns 
 */
var maxProduct2 = function (nums) {
    let n = nums.length;
    let dp = new Array(n).fill(0)
    for (let i = 0; i < n; i++) {
        if (nums[i] == 0) {
            dp[i] = 0;
            continue;
        }
        if (!dp[i - 1]) {
            dp[i] = nums[i];
        } else {
            dp[i] = dp[i - 1] * nums[i];
        }
    }

    let max = Math.max(...nums);
    // 因为0需要特殊处理, 因此, for 里面需要注意: dp需要按0分成多个小数组, 每个小数组的前一个元素设置为1,
    for (let i = 0; i < n; i++) {
        if (dp[i] == 0) {
            continue;
        }
        for (let j = i + 1; j < n; j++) {
            // 如果当前dp[j]为0, 表示nums[i] = 0, 已经到达小数组的最后一条元素, 则可以跳出内循环
            if (dp[j] == 0) {
                break;
            }
            // 这里的 || 是当i为小数组的第一个元素的时候上个元素应该设置为1
            var lastDp = dp[i - 1] || 1
            max = Math.max(max, dp[j] / lastDp);
        }
    }
    return max;
};
console.info(maxProduct([1, 2, -1, 4, -2, -3, 2]));