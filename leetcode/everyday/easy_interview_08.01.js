/**
 * @param {number} n
 * @return {number}
 */
var waysToStep = function (n) {
    let dp = new Array(n).fill(0);
    dp[0] = 1;
    dp[1] = 2;
    dp[2] = 4;
    for (let i = 3; i < n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007
    }
    return dp[n - 1];
};