# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res=[root.val]

        def dfs(root):
            # 递归(recursion) 之前，要写清楚边界条件
            if not root:
                return 0
            leftMax=dfs(root.left)
            rightMax=dfs(root.right)
            leftMax=max(leftMax,0) #注意负数的情况，就不更新了
            rightMax=max(rightMax,0)

            res[0]=max(res[0],root.val+leftMax+rightMax)#更新的值，和返回的值不一样

            return root.val + max(leftMax,rightMax) #返回没有split的值
        
        dfs(root)
        return res[0]

            
            