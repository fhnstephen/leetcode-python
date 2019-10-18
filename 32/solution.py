class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        f = [0 for _ in range(n)]
        ans = 0
        for i, ch in enumerate(s):
            cur = 0
            if ch == ')':
              if i - 1 >= 0:
                  if s[i - 1] == '(':
                      if i - 2 >= 0:
                          cur = f[i - 2] + 2
                      else:
                          cur = 2
                  else:
                      left = i - f[i - 1] - 1
                      if left >= 0 and s[left] == '(':
                          cur = f[i - 1] + 2
                          if left >= 1:
                              cur += f[left - 1]
            f[i] = cur
            ans = max(ans, cur)
        return ans


