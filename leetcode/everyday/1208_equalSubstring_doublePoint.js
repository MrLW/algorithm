const { endianness } = require("os");
const { start } = require("repl");

/**
 *  双指针
 */
var equalSubstring = function (s, t, maxCost) {
    let len = s.length;
    let maxCount = 0;
    let left = 0, right = 0;
    let nums = [];
    for (let i = 0; i < s.length; i++) {
        nums.push(Math.abs(s[i].charCodeAt() - t[i].charCodeAt()))
    }
    let sum = 0;
    while (right < len) {
        sum += nums[right];
        while (sum > maxCost) {
            sum -= nums[left];
            left++;
        }
        maxCount = Math.max(maxCount, right - left + 1);
        right++
    }
    return maxCount;
};
let s = "tyiraojpcfuttwblehv", t = "stbtakjkampohttraky", cost = 119
const result = equalSubstring(s, t, cost);
console.info(result);
