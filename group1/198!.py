class Solution:
    # dp[i] = num[i],i =0; max(num[i-1],num[i]),i=2
    # dp[i] = max(dp[i-2]+num[i],dp[i-1])
    def rob(self, nums: List[int]) -> int:
        p = 0
        q = 0
        r = 0

        for i, num in enumerate(nums):
            r = max(p+num, q)
            p = q
            q = r

        return r
