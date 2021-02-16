/**
 *  种花问题
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let len = flowerbed.length;
    let i = 0 , lastFlowerbed = false;
    while (i < len) {
        // 上一次种花了, 本次又种花
        let canPlace = flowerbed[i++] == 0;
        if(n < 0){
            break;
        }
        if(!canPlace && lastFlowerbed){
            n++;
            lastFlowerbed = true;
            continue;
        }
        // 当前已经种花
        if(!canPlace){
            lastFlowerbed = true;
            continue;
        }
        // 上一个种花了
        if(lastFlowerbed){
            lastFlowerbed = false;
            continue;
        }
        // 上一次没有种花 && 本次可以中
        if(!lastFlowerbed && canPlace){
            n--;
            lastFlowerbed = true;
        }
    }
    return n <= 0;
};

const nums = [0,0,1,0,0], n = 1;
//[1, 0, 0, 0, 0, 1, 0, 0] 2
//[1, 0, 1, 0, 0, 1, 0, 0]
//[1, 0, 1, 0, 1, 1, 0, 0]
console.info(canPlaceFlowers(nums,n));