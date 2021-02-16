/**
 * 情侣牵手
 * @param {*} row 
 */
var minSwapsCouples = function(row) {
    // 3,2,4,1,0,5
    let dic = {};
    row.forEach((value, index)=>dic[value] = index);
    let pos = 0, count = 0;
    let newRow = new Array(row.length);
    newRow.fill(0);
    while(pos< row.length){
        let needSort = Math.max(row[pos], row[pos+1]) % 2 == 0;
        let isOdd1 = row[pos] % 2 == 1;
        let isOdd2 = row[pos+1] % 2 == 1;
        if(isOdd1 && isOdd2 || (!isOdd1 && !isOdd2)){
            // 两个数都是奇数 or 两个数都是偶数, **保证最大值是奇数**
            let j = pos, i = row[pos+1] % 2 == 0 ? dic[row[pos+1] + 1]: dic[row[pos+1] - 1]
            // 如果第pos已经保证了顺序, 则交换pos+1的值
            if(!newRow[row[pos]]) {
                j = pos+1; i = row[pos] % 2 == 0 ? dic[row[pos] + 1]: dic[row[pos] - 1]
            }
            swap(row, dic, j, i);
            count++;
        } else if(needSort){
            // 1 奇数 or 1 偶数
            let j = pos, v = dic[row[pos+1] + 1];
            // 较大值是偶数, 将较小值-1和较大值交换
            [j, v] = row[pos+1] > row[pos] ? [pos+1, dic[row[pos]-1]] : [pos, dic[row[pos+1] -1] ];
            swap(row, dic, j, v);
            count++;
        } else if(Math.abs(row[pos]-row[pos+1]) != 1) {
            // 1个数是奇数, 1个数是偶数, 但是非相邻
            let j = pos, v = row[pos+1] % 2 == 0 ?  dic[row[pos+1] + 1]:  dic[row[pos+1] + 1]
            if(!newRow[row[pos]]) {
                j = pos+1; v = row[pos] % 2 ==0? dic[row[pos] + 1]: dic[row[pos] - 1];
            }
            swap(row, dic, j, v);
            count++;    
        }
        newRow[row[pos]-1] = row[pos]; 
        newRow[row[pos+1]-1] = row[pos+1]; 
        pos = pos + 2;
    }
    return count;
};
var swap = function(row,dic, i, j) {
    let temp = row[i];
    row[i] = row[j];
    row[j] = temp;
    temp = null;
    
    dic[row[i]] = i;
    dic[row[j]] = j;
}
// 最大值 2 * i + 1
// 奇数为男, 偶数为女

let row = [5,6,4,0,2,1,9,3,8,7,11,10];
// let row = [3, 2, 0, 1]


// 5,6,0,2,4 ,1,9,3,8,7,11,10


//0,2,4,6,7,1,3,5

//0,1,4,6,7,2,3,5
//0,1,4,5,7,2,3,6
//0,1,4,5,7,6,3,2
const result = minSwapsCouples(row);
console.info(result);