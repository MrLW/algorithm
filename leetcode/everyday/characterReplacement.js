/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
    // left 、right分别为左右指针, seq为每个字符出现的次数
    let left = 0, right = 0, len = s.length, seq = [];
    let maxCount = 0;
    for (let i = 0; i < 26; i++) {
        seq[i] = 0;
    }
    while (right < len) {
        // 1. 计算每个字符出现的次数
        let pos = s[right].charCodeAt() - 'A'.charCodeAt();
        seq[pos]++;
        // 2. 右指针 - 左指针 - 最大相同子串 = 不同于最大相同子串 > k, 则需要左指针左移动, 右指针移动
        if (right - left + 1 - Math.max(...seq) > k) {
            seq[s[left].charCodeAt() - 'A'.charCodeAt()]--;
            left++;
        } else {
            maxCount = Math.max(maxCount, right - left + 1);
        }
        right++;
    }
    return maxCount;
};
let s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", k = 4;
const result = characterReplacement(s, k);
console.info(result);