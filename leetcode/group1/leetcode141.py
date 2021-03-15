# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur1 = head
        cur2 = head

        while(cur1 or cur2):
            cur1 = cur1 and cur1.next and cur1.next.next
            cur2 = cur2 and cur2.next

            if not (cur1 or cur2):
                return False

            if (cur1 is cur2):
                return True
        return False
