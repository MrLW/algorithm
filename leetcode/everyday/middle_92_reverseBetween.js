/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {
    const result = new ListNode(-1);
    result.next = head;
    let pre = result;
    // leftNode: 左节点; rightNode: 右节点; pre: 前驱节点; suss: 后继节点
    for (let i = 0; i < left - 1; i++) {
        pre = pre.next;
    }
    let rightNode = pre;
    for (let i = 0; i < right - left + 1; i++) {
        rightNode = rightNode.next;
    }
    let leftNode = pre.next;
    let succ = rightNode.next;
    rightNode.next = null;
    pre.next = null;
    let mid = reverseList(leftNode);
    pre.next = mid;
    leftNode.next = succ;
    return result.next;
};

// 反转列表
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





// 这个算法修改了链表的值, 速度慢, 不推荐
// 113ms
// var reverseBetween = function (head, left, right) {
//     let arr = [];
//     let temp = head;
//     let i = 1;
//     while (temp) {
//         if(i > right){
//             break;
//         }
//         if (i >= left && i <= right) {
//             arr.push(temp.val);
//         }
//         temp = temp.next
//         i++;
//     }
//     temp = head;
//     i = 1;
//     let result = temp;
//     while (temp) {
//         if(i > right){
//             break;
//         }
//         if (i >= left && i <= right) {
//             temp.val = arr.pop();
//         }
//         temp = temp.next
//         i++;
//     }
//     return result;
// };

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next)
}

let head = [1, 2, 3, 4, 5], left = 2, right = 4
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

reverseBetween(first.next, left, right)



console.info(first.next)