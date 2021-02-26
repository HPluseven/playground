# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        def reverse(pre, cur):
            next = cur.next
            cur.next = pre
            if not next:
                return cur
            return reverse(cur, next)

        return reverse(None, head)

# no recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        pre = None
        cur = head

        if not cur.next:
            return cur
        
        while cur:
            rear = cur.next
            cur.next = pre
            pre = cur
            cur = rear

        return pre

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    s = Solution()
    r = s.reverseList(head)
    print(r.next)
