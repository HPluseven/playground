/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  let quickPoint = head;
  let slowPoint = head;

  while (quickPoint && slowPoint) {
    slowPoint = slowPoint.next;
    quickPoint = quickPoint.next && quickPoint.next.next;
    if (quickPoint !== null && quickPoint === slowPoint) {
      return true;
    }
  }

  return false;
};
