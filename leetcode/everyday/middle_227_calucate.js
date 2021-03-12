/**
 * 基本计算器 II
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
    let numsStack = [], charStack = [], lastIsNum = false, shouldCal = false;
    s = s.trim();
    for (let i = 0; i < s.length; i++) {
        if (s[i] == ' ') {
            continue;
        }
        // 如果 第i个元素是数字
        if (s[i].charCodeAt() >= 48 && s[i].charCodeAt() <= 57) {
            if (!lastIsNum) {
                numsStack.push(parseInt(s[i]))
            } else {
                let old = numsStack.pop();
                let _new = old * 10 + parseInt(s[i]);
                numsStack.push(_new);
            }
            lastIsNum = true;
            if (i != s.length - 1) {
                continue;
            }
        }
        // 此时是否应该计算 乘除
        if (shouldCal) {
            let x = numsStack.pop();
            let y = numsStack.pop();
            let char = charStack.pop();
            if (char == '*') {
                numsStack.push(x * y);
            } else if (char == '/') {
                numsStack.push(parseInt(y / x));
            }
            shouldCal = false;
        }
        // 如果当前元素是 乘除 则将
        if (s[i] == '*' || s[i] == '/') {
            shouldCal = true;
        }
        charStack.push(s[i]);
        lastIsNum = false;
    }
    let i = 0;
    // 计算剩下的加减算法
    while (i < numsStack.length - 1) {
        let x = numsStack[i]
        let y = numsStack[i + 1];
        let char = charStack[i]
        if (char == '+') {
            numsStack[i + 1] = x + y;
        } else if (char == '-') {
            numsStack[i + 1] = x - y;
        }
        i++;
    }
    return numsStack[numsStack.length - 1];
    // 3+2*2 =>
    // numStack     : 3 2 2
    // charStack    : + *
    // 2*2+3 =>
    // numStack     : 2 2 3
    // charStack    : * +

};
(async () => {
    console.info('0:', '0'.charCodeAt())
    console.info('9:', '9'.charCodeAt())
    console.info(calculate(" 30 - 200 / 100 + 2 * 3 "))
})()
