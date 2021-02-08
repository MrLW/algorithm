/**
 * @param {string[]} A
 * @param {string[]} B
 * @return {string[]}
 */
var wordSubsets = function (A, B) {

    let AData = [], BData = [];
    for (let aWord of A) {
        let aWordSeq = {};
        for (let letter of aWord) {
            aWordSeq[letter] = (aWordSeq[letter] || 0) + 1;
        }
        AData.push(aWordSeq)
    }
    // console.info(AData)
    for (let bWord of B) {
        let bWordSeq = {};
        for (let letter of bWord) {
            bWordSeq[letter] = (bWordSeq[letter] || 0) + 1;
        }
        BData.push(bWordSeq)
        
    }
    console.info(AData)
    for(let item of AData){
        
    }

};
const A = ["amazon", "apple", "facebook", "google", "leetcode"], B = ["e", "o"];
const result = wordSubsets(A, B);
console.info('result', result);