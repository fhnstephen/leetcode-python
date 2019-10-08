# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
      def dfs(cur):
        if cur is None:
          return (-10000000000, -10000000000)
        if cur.left is None and cur.right is None:
          return (cur.val, cur.val)
        left = dfs(cur.left)
        right = dfs(cur.right)
        max_val_root = max([left[0] + cur.val, right[0] + cur.val, cur.val])
        max_val_no_root = max([left[1], right[1], max_val_root, left[0] + cur.val + right[0]])
        return (max_val_root, max_val_no_root)
      ans = dfs(root)
      return ans[1]
