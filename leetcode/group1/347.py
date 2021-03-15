import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = defaultdict(int)
        heap = []
        for num in nums:
            occ[num] += 1

        for num, freq in occ.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif heap[0][0] < freq:
                heapq.heapreplace(heap, (freq, num))

        return [item[1] for item in heap]


s = Solution()
print(s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
