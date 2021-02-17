/**
 * 滑动窗口最大值
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
  let queue = new PriorityQueue((a, b) => a > b);
  // 初始化
  let result = [];
  for (let i = 0; i < k; i++) {
    queue.offer(nums[i]);
  }
  result.push(queue.peek());
  for (let i = k; i < nums.length; i++) {
    queue.remove(nums[i - k]);
    queue.offer(nums[i]);
    result.push(queue.peek());
  }
  return result;
};

class PriorityQueue {
  constructor(comparator) {
    this.data = [];
    this.size = 0;
    this.comparator = comparator;
  }

  offer(e) {
    if (this.size == 0) {
      this.data[0] = e;
    } else {
      this.siftUp(this.size, e);
    }

    this.size++;
  }

  siftUp(k, e) {
    while (k > 0) {
      let parent = Math.floor((k - 1) >> 1);
      if (this.comparator(this.data[parent], e)) {
        break;
      }
      this.data[k] = this.data[parent];
      k = parent;
    }
    this.data[k] = e;
  }

  poll() {
    if (this.size == 0) return null;
    let result = this.data[0];
    this.size--;
    // 取出最后一个元素
    let x = this.data.pop();
    if (this.size != 0) {
      this.siftDown(0, x);
    }

    return result;
  }

  siftDown(k, e) {
    let half = this.size >>> 1;
    while (k < half) {
      let child = (k << 1) + 1;
      let c = this.data[child];
      let right = child + 1;
      if (right < this.size && this.comparator(this.data[right], c)) {
        c = this.data[(child = right)];
      }
      if (this.comparator(e, c)) {
        break;
      }
      this.data[k] = c;
      k = child;
    }
    this.data[k] = e;
  }

  peek() {
    if (this.size == 0) return null;
    return this.data[0];
  }

  remove(e) {
    let i = this.indexOf(e);
    if (i == -1) return false;
    this.size--;
    if (this.size == i) {
      this.data.pop();
    } else {
      let moved = this.data.pop();
      this.siftDown(i, moved);
      if(this.data[i] == moved){
        this.siftUp(i, moved);
      }
    }
  }

  indexOf(e) {
    for (let i = 0; i < this.size; i++) {
      if (this.data[i] == e) {
        return i;
      }
    }
    return -1;
  }
}
(async () => {
  let nums = [
      7629,
      5877,
      3338,
      8899,
      4223,
      -8068,
      3775,
      7954,
      8740,
      4567,
      6280,
      -7687,
      -4811,
      -8094,
      2209,
      -4476,
      -8328,
      2385,
      -2156,
      7028,
      -3864,
      7272,
      -1199,
      -1397,
      1581,
      -9635,
      9087,
    ],
    k = 6;
  console.info(maxSlidingWindow(nums, k));
})();
// [1,3,-1,-3,5,3,6,7]
