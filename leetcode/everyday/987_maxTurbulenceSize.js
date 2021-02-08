/**
 * @param {number[]} arr
 * @return {number}
 */
var maxTurbulenceSize = function (arr) {
    let maxCount = 1, left = 0, right = 1, len = arr.length, cur, last;
    if (len == 1) return 1;
    while (right < len) {
        if (arr[right] == arr[right - 1]) {
            left = right++;
            continue;
        }
        cur = arr[right] > arr[right - 1];
        if (left != right - 1 && cur == last) {
            left++;
        } else {
            maxCount = Math.max(maxCount, right - left + 1);
            right++;
        }
        last = cur;

    }
    return maxCount;
};
const arr = [2, 0, 2, 4, 2, 5, 0, 1, 2, 3];
const result = maxTurbulenceSize(arr);
console.info(result);