class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      n = len(nums)
      nums.sort()
      ans = None
      for i, num in enumerate(nums):
        j = i + 1
        k = n - 1
        while j < k:
          sum = num + nums[j] + nums[k]
          distance = abs(sum - target)
          if ans is None or distance < ans[0]:
            ans = (distance, sum)
          if sum > target:
            k = k - 1
          else:
            j = j + 1
      return ans[1]
