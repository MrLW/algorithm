/**
 * 暴力法
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function (s, t, maxCost) {
    let len = Math.min(s.length, t.length);
    let maxCount = 0;
    let left = 0, right = left;
    while (left < (len - maxCount)) {
        let sub = 0;
        while (sub <= maxCost && right < len) {
            sub += Math.abs(s[right].charCodeAt() - t[right].charCodeAt());
            right++
        }
        // 如果 子串的字符之差 超过了 maxCount
        if (sub > maxCost) {
            right--;
        }
        maxCount = Math.max(maxCount, right - left);
        // 重置right
        right = ++left;

    }
    return maxCount;
};
let s = "krpgjbjjznpzdfy", t = "nxargkbydxmsgby", cost = 14
const result = equalSubstring(s, t, cost);
console.info(result);
