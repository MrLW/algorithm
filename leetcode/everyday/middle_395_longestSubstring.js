/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function (s, k) {
    let map = {};
    for (let c of s) {
        map[c] = (map[c] || 0) + 1;
    }
    for (let c of Object.keys(map)) {
        if (map[c] < k) {
            let res = 0;
            for (let t of s.split(c)) {
                res = Math.max(res, longestSubstring(t, k));
            }
            return res;
        }
    }
    return s.length;
};

// let s = "ababbc", k = 2;
let s = "aaabb", k = 3
//
console.info(longestSubstring(s, k))