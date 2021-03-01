import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(node.val, idx, node)
                for idx, node in enumerate(lists) if node]
        heapq.heapify(heap)
        res = None
        cur = res

        while(len(heap) > 0):
            _, idx, min_node = heapq.heappop(heap)
            if cur:
                cur.next = min_node
                cur = cur.next
            else:
                res = min_node
                cur = res
            next_node = min_node.next
            if next_node:
                heapq.heappush(heap, (next_node.val, idx, next_node))
        return res
