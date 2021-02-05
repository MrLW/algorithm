
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var medianSlidingWindow = function (nums, k) {
    let dh = new DualHeap(k);
    for (let i = 0; i < k; i++) {
        dh.insert(nums[i])
    }
    let result = [dh.getMedian()];
    for (let i = k; i < nums.length; ++i) {
        dh.insert(nums[i]);
        dh.erase(nums[i - k]);
        result[i - k + 1] = dh.getMedian();
    }
    return result;
};

class DualHeap {

    constructor(k) {
        // 最小堆
        this.small = new PriorityQueue((a, b) => a > b);
        this.smallSize = 0;
        // 最大堆
        this.large = new PriorityQueue((a, b) => a <= b);
        this.largetSize = 0;
        this.delayed = {};
        this.k = k;
    }

    insert(num) {
        if (this.small.isEmpty() || num <= this.small.peek()) {
            this.small.offer(num)
            this.smallSize++;
        } else {
            this.large.offer(num);
            this.largetSize++;
        }
        this.makeBalance()
    }

    makeBalance() {
        if (this.smallSize - this.largetSize > 1) {
            this.large.offer(this.small.poll());
            --this.smallSize;
            ++this.largetSize;
            this.prune(this.small)
        } else if (this.smallSize < this.largetSize) {
            this.small.offer(this.large.poll());
            --this.largetSize;
            ++this.smallSize;
            this.prune(this.large)
        }
    }

    erase(num) {
        this.delayed[num] = this.delayed[num] || 0 + 1
        if (num <= this.small.peek()) {
            --this.smallSize;
            if (num == this.small.peek()) {
                this.prune(this.small);
            };
        } else {
            --this.largetSize;
            if (num == this.large.peek()) {
                this.prune(this.large)
            }
        }
        this.makeBalance()
    }

    prune(heap) {
        while (!heap.isEmpty()) {
            let num = heap.peek();
            if (this.delayed[num]) {
                this.delayed[num] = this.delayed[num] - 1;
                if (this.delayed[num] == 0) {
                    delete this.delayed[num];
                }
                heap.poll();
            } else {
                break;
            }
        }
    }

    getMedian() {
        return (this.k & 1) == 1 ? this.small.peek() : (this.small.peek() + this.large.peek()) / 2;
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
        if (e == null) {
            throw new Error('元素不可以为null')
        };
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
            if (right < this.size && this.comparator(this.queue[right], c)) {
                c = this.queue[child = right]
            }

            if (this.comparator(e, c)) {
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

let data = [7, 0, 3, 9, 9, 9, 1, 7, 2, 3], k = 6;
(async () => {
    // 2, 3, 3, 3,2,3,2
    const result = medianSlidingWindow(data, k);
    console.info(result);
})()
