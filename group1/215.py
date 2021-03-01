class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap_size = len(nums)
        self.buld_max_heap(nums, heap_size)
        if k > len(nums):
            return nums[0]
        for _ in range(0, k-1):
            nums[0], nums[heap_size-1] = nums[heap_size-1], nums[0]
            heap_size -= 1
            self.max_heapify(nums, 0, heap_size)
        return nums[0]

    def buld_max_heap(self, a, heap_size):
        for i in range(heap_size//2, -1, -1):
            self.max_heapify(a, i, heap_size)

    def max_heapify(self, a, i, heap_size):
        l, r, largest = i*2+1, i*2+2, i
        if l < heap_size and a[l] > a[largest]:
            largest = l
        if r < heap_size and a[r] > a[largest]:
            largest = r

        if i != largest:
            a[i], a[largest] = a[largest], a[i]
            self.max_heapify(a, largest, heap_size)


s = Solution()
nums = [2, 1]
print(s.findKthLargest(nums, 2))
