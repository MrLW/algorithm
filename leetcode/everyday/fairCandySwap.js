/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var fairCandySwap = function (A, B) {
    // 分别计算A、B的总大小
    let sumA = 0, sumB = 0;
    for (let x = 0; x < A.length; x++) {
        sumA += A[x]
    }
    for (let x = 0; x < B.length; x++) {
        sumB += B[x]
    }
    for (let i = 0; i < A.length; i++) {
        for (let j = 0; j < B.length; j++) {
            // A 加上B交换过来的糖果
            let newA = sumA - A[i] + B[j];
            // B 加上A交换过来的糖果
            let newB = sumB - B[j] + A[i];
            if (newA == newB) {
                return [A[i], B[j]];
            }
        }
    }
    return null;
};

(async () => {
    let A = [1, 2, 5], B = [2, 4]
    console.info(fairCandySwap(A, B));
})()