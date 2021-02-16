/**
 * 两数相加
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let r1 = l1,
    r2 = l2;
  let isAddOne = 0,
    lastNode = null;
  let result = new ListNode(0);
  while (r1 && r2) {
    let singleSum = r1.val + r2.val + isAddOne;
    if (singleSum > 9) {
      // 进1
      isAddOne = 1;
    } else {
      isAddOne = 0;
    }
    r1.val = singleSum % 10;
    if (lastNode) {
      lastNode.next = r1;
    } else {
      result.next = r1;
    }
    lastNode = r1;
    r1 = r1.next;
    r2 = r2.next;
  }
  while (r1) {
    let singleSum = r1.val + isAddOne;
    if (singleSum > 9) {
      // 进1
      isAddOne = 1;
    } else {
      isAddOne = 0;
    }
    r1.val = singleSum % 10;
    if (lastNode) {
      lastNode.next = r1;
    } else {
      result.next = r1;
    }
    lastNode = r1;
    r1 = r1.next;
  }
  while (r2) {
    let singleSum = r2.val + isAddOne;
    if (singleSum > 9) {
      // 进1
      isAddOne = 1;
    } else {
      isAddOne = 0;
    }
    r2.val = singleSum % 10;
    if (lastNode) {
      lastNode.next = r2;
    } else {
      result.next = r2;
    }
    lastNode = r2;
    r2 = r2.next;
  }
  if(isAddOne){
    lastNode.next = new ListNode(1);
  }
  return result.next;
};

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}
(async () => {
  // 2 4 3
  // 5 6 4
  let l1 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))));
  let l2 = new ListNode(
    9,
    new ListNode(
      9,
      new ListNode(
        9,
        new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))))
      )
    )
  );
  // 342 +
  // 465 =
  // 807

  // 9999
  // 9999999
  // 8999001
  addTwoNumbers(l1, l2);
})();
