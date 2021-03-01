/**
 * @param {number[]} nums
 */
var NumArray = function (nums) {
    this.sums = new Array(nums.length + 1).fill(0);
    for (let i = 0; i < nums.length; i++) {
        this.sums[i + 1] = this.sums[i] + nums[i];
    }
    console.log(this.sums);
};

/** 
 * @param {number} i 
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function (i, j) {
    return this.sums[j + 1] - this.sums[i];
};

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(i,j)
 */

// ["NumArray","sumRange","sumRange","sumRange"]
// [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

let obj = new NumArray([-2, 0, 3, -5, 2, -1]);
obj.sumRange(0, 2)