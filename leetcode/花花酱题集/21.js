/**
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
var mergeTwoLists = function (l1, l2) {
  if (!l1 || !l2) return l1 || l2;

  let p1 = l1;
  let p2 = l2;

  const res = new ListNode();
  let p = res;

  while (p1 && p2) {
    if (p1.val < p2.val) {
      p.next = new ListNode(p1.val);
      p = p.next;
      p1 = p1.next;
    } else if (p1.val === p2.val) {
      p.next = new ListNode(p1.val, new ListNode(p2.val));
      p = p.next.next;
      p1 = p1.next;
      p2 = p2.next;
    } else {
      p.next = new ListNode(p2.val);
      p = p.next;
      p2 = p2.next;
    }
  }

  if (!p1 || !p2) p.next = p1 && p2;

  return res.next;
};
