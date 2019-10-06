class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = None
        cur = 0
        for num in nums:
          cur += num
          if ans is None or cur > ans:
            ans = cur
          if cur < 0:
            cur = 0
        return ans
