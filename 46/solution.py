class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      def backtrace(pos = 0):
        if pos == n:
          ans.append(nums[:])
          return
        for i in range(pos, n):
          nums[pos], nums[i] = nums[i], nums[pos]
          backtrace(pos + 1)
          nums[pos], nums[i] = nums[i], nums[pos]
      ans = []
      n = len(nums)
      backtrace()
      return ans


class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        self.temp_ans = [None for x in range(len(nums))]
        self.used = {}
        self.dfs(0)
        return self.ans

    def dfs(self, pos):
        if pos == len(self.nums):
          self.ans.append(self.temp_ans[:])
          return
        for i in self.nums:
          if not self.used.get(i, False):
            self.temp_ans[pos] = i
            self.used[i] = True
            self.dfs(pos + 1)
            self.used[i] = False
