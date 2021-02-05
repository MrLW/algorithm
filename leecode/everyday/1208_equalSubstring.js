/**
 * 暴力法
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function (s, t, maxCost) {
    let len = s.length;
    let maxCount = 0;
    let left = 0, right = 0;
    let nums = [];
    for (let i = 0; i < s.length; i++) {
        nums.push(Math.abs(s[i].charCodeAt() - t[i].charCodeAt()))
    }
    while (right < len) {
        if (nums.slice(left, right + 1).reduce((a, b) => a + b) > maxCost) {
            left++;
        }
        right++;
        maxCount = Math.max(maxCount, right - left);
    }
    return maxCount;
};
let s = "tyiraojpcfuttwblehv", t = "stbtakjkampohttraky", cost = 119
const result = equalSubstring(s, t, cost);
console.info(result);
