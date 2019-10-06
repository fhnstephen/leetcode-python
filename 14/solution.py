class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        ans = ""
        if len(strs) == 0:
          return ans
        while True:
          flag = True
          cur = None
          for str in strs:
            if i >= len(str):
              return ans
            if cur is None or str[i] == cur:
              cur = str[i]
            else:
              flag = False
              break
          if flag:
            ans += cur
          else:
            return ans
          i += 1
