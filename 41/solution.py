class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 1
        for num in nums:
          if num == 1:
            break
        if num != 1:
          return 1
        for i, num in enumerate(nums):
          if num > n or num <= 0:
            nums[i] = 1
        for num in nums:
          if nums[abs(num) - 1] > 0:
            nums[abs(num) - 1] = -nums[abs(num) - 1]
        for i, num in enumerate(nums):
          if num > 0:
            return i + 1
        return n + 1
