/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function (s, k) {
    let ret = 0;
    const n = s.length;
    // 这层for 是依次判断最长子串种类的数量
    for (let t = 1; t <= 26; t++) {
        let l = 0, r = 0;
        const cnt = new Array(26).fill(0);
        let tot = 0;
        // 表示当前次数小余k的字符的数量
        let less = 0;
        while (r < n) {
            // 当前右指针字符出现的数量+1
            cnt[s[r].charCodeAt() - 'a'.charCodeAt()]++;
            // 当前字符次数第一次出现 less+1 ; 字符总类数量tot+1
            if (cnt[s[r].charCodeAt() - 'a'.charCodeAt()] === 1) {
                tot++;
                less++;
            }
            // 当前字符出现的次数等于k, 所以 less-1
            if (cnt[s[r].charCodeAt() - 'a'.charCodeAt()] === k) {
                less--;
            }
            // 当字符种类数量 > 给定的字符种类数量时 左指针向右移动
            while (tot > t) {
                // 当前左指针字符的数量-1
                cnt[s[l].charCodeAt() - 'a'.charCodeAt()]--;
                // 表示当前字字符之前还是满足题目要求, 优惠上一步减一了则又不满足题要求了, 因此需要less-1(即小余k的字符的数量+1)
                if (cnt[s[l].charCodeAt() - 'a'.charCodeAt()] === k - 1) {
                    less++;
                }
                // 当前左指针字符的数量已经没有了, 则字符总数量-1 && 小余k的字符的数量-1(因为这个字符已经没有了)
                if (cnt[s[l].charCodeAt() - 'a'.charCodeAt()] === 0) {
                    tot--;
                    less--;
                }
                // 左指针右移动
                l++;
            }
            // 小余k的字符的数量已经没有
            if (less == 0) {
                // 计算子串大小
                ret = Math.max(ret, r - l + 1);
            }
            r++;
        }
        console.info('ret:', ret);
    }
    return ret;
};

// let s = "ababbc", k = 2;
let s = "ababbc", k = 2
//
console.info(longestSubstring(s, k))