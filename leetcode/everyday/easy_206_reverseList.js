/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
    // cur: 当前节点; pre: 上一个节点
    let cur = head, pre = null;
    while (cur) {
        // 记录当前节点后面节点, 防止后面被删除
        let tmp = cur.next
        // 当前节点的下一个节点指向上一个接地那
        cur.next = pre;
        // 当前节点设置为上一个节点
        pre = cur;
        // 将后续节点设置为当前节点
        cur = tmp;
    }
    return pre;
};

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next)
}

let head = [1, 2, 3, 4, 5];
let first = new ListNode(-1), pre;
for (let i = 0; i < head.length; i++) {
    let node = new ListNode(head[i]);
    if (i == 0) {
        first.next = node;
    } else {
        pre.next = node;
    }
    pre = node;
}

reverseList(first.next)

