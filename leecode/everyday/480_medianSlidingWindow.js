const { exception } = require("console");

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var medianSlidingWindow = function (nums, k) {
    let len = nums.length;
    if (nums.length == 0 || k > len) return [];
    let left = 0, right = k;
    let result = [];
    let isOdd = k % 2 == 1
    while (right <= len) {
        // 暴力法 这里可以直接排序 nums.slice(left, right), 不推荐, 经测试内存吃不消
        let windows = nums.slice(left, right);
        if (isOdd) {
            result.push(windows[Math.floor(k / 2)]);
        } else {
            let i = k / 2 - 1;
            result.push((windows[i] + windows[i + 1]) / 2)
        }
        left += 1;
        right += 1
    }
    return result;
};

class DualHeap {

    constructor() {
        // 最小堆
        this.small = new PriorityQueue((a, b) => a > b);
        this.smallSize = 0;
        // 最大堆
        this.larget = new PriorityQueue((a, b) => a <= b);
        this.largetSize = 0;
    }

    insert(num) {
        if (this.small.isEmpty() || num <= this.small.peek()) {
            this.small.offer(num)
            this.smallSize++;
        } else {
            this.larget.offer(num);
            this.largetSize++;
        }
        this.makeBalance()
    }

    makeBalance() {
        if (this.smallSize - this.largetSize > 1) {
            this.larget.offer(this.small.poll());
            --this.smallSize;
            ++this.largetSize;
        } else if (this.smallSize < this.largetSize) {
            this.small.offer(this.larget.poll());
            --this.largetSize;
            ++this.smallSize;
        }
    }

    print() {
        console.info('small', this.small.queue)
        console.info('larget', this.larget.queue)
    }
}

/**
 *  维护一个优先队列
 */
class PriorityQueue {

    constructor(comparator) {
        this.queue = [];
        this.size = 0;
        this.comparator = comparator;
    }

    offer(e) {
        if (!e) throw new exception('元素不可以为null');
        if (!this.size) {
            this.queue[0] = e;
        } else {
            this.siftUp(this.size, e)
        }
        this.size++;
    }

    /**
     * 调整
     * @param {*} k 新插入元素后数组的最后一个元素的位置
     * @param {*} e 新插元素
     */
    siftUp(k, e) {
        while (k > 0) {
            let parent = (k - 1) >>> 1;
            //this.queue[parent] < e
            if (this.comparator(this.queue[parent], e)) {
                break;
            }
            this.queue[k] = this.queue[parent];
            k = parent;
        }
        return this.queue[k] = e;
    }

    poll() {
        if (this.size == 0) return null;
        let result = this.queue[0];
        this.size--
        let x = this.queue.pop();
        if (this.size != 0) {
            this.siftDown(0, x);
        }
        return result;
    }

    siftDown(k, e) {
        let half = this.size >>> 1;
        while (k < half) {
            let child = (k << 1) + 1;
            let c = this.queue[child];
            let right = child + 1;
            if (right < this.size && c > this.queue[right]) {
                c = this.queue[child = right]
            }

            if (e < c) {
                break;
            }
            this.queue[k] = c;
            k = child;
        }
        this.queue[k] = e;
    }

    peek() {
        if (this.size == 0) return null;
        return this.queue[0];
    }

    isEmpty() {
        return this.size == 0;
    }
}

let data = [1, 3, -1, -3, 5, 3, 6, 7], k = 8;
(async () => {
    let dh = new DualHeap();
    for (let i = 0; i < k; i++) {
        dh.insert(data[i])
    }
    dh.print();
})()
