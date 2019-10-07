class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(pos = 0, last = -1):
          ans.append(cur[:])
          if pos == n:
            return
          for i in range(last + 1, n):
            cur.append(nums[i])
            dfs(pos + 1, i)
            del cur[pos]

        cur = []
        ans = []
        n = len(nums)
        dfs()
        return ans

