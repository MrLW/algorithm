/**
 *  前缀和
 */
var equalSubstring = function (s, t, maxCost) {
    const n = s.length;
    const accDiff = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        accDiff[i + 1] = accDiff[i] + Math.abs(s[i].charCodeAt() - t[i].charCodeAt());
    }
    let maxLength = 0;
    for (let i = 1; i <= n; i++) {
        const start = binarySearch(accDiff, i, accDiff[i] - maxCost);
        maxLength = Math.max(maxLength, i - start);
    }
    return maxLength;
};

const binarySearch = (accDiff, endIndex, target) => {
    let low = 0, high = endIndex;
    while (low < high) {
        const mid = Math.floor((high - low) / 2) + low;
        if (accDiff[mid] < target) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}

let s = "abcd", t = "bcdf", cost = 3;
const result = equalSubstring(s, t, cost);
console.info(result);
