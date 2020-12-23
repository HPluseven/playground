# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# recursive


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         def add(node1, node2, carry, node):
#             if not node1 and not node2:
#                 if carry == 0:
#                     return
#                 else:
#                     node.next = ListNode(carry)

#             if node1 and not node2:
#                 sum_ = node1.val + carry
#                 carry = sum_ // 10
#                 node.next = ListNode(sum_ % 10)
#                 add(node1.next, None, carry, node.next)

#             if node2 and not node1:
#                 sum_ = node2.val + carry
#                 carry = sum_ // 10
#                 node.next = ListNode(sum_ % 10)
#                 add(None, node2.next,  carry, node.next)

#             if node2 and node1:
#                 sum_ = node1.val + node2.val + carry
#                 carry = sum_ // 10
#                 node.next = ListNode(sum_ % 10)
#                 add(node1.next, node2.next, carry, node.next)

#         head = ListNode(-1)
#         add(l1, l2, 0, head)
#         return head.next

# no recursive


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)

        cur1, cur2 = l1, l2
        carry = 0
        node = head

        while cur1 or cur2:
            val1 = (cur1 and cur1.val) or 0
            val2 = (cur2 and cur2.val) or 0

            sum_ = val1 + val2 + carry
            carry = sum_ // 10
            node.next = ListNode(sum_ % 10)
            cur1 = cur1 and cur1.next
            cur2 = cur2 and cur2.next
            node = node.next

        if carry:
            node.next = ListNode(carry)

        return head.next
