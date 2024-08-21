class Treenode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# dp[i]：考虑下标i（包括i）以内的房屋，最多可以偷窃的金额为dp[i]
class Solution:
    def rob1(self, nums: list[int]) -> int:
        # 1.打家劫舍一：相邻不可偷
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
    

    def rob2(self, nums: list[int]) -> int:
        # 2.打家劫舍二：相邻不可且首尾环形相连
        # 对于成环的数组，考虑3种(2种)情况，不包含（抢）首尾，考虑抢首不抢尾，抢尾不抢首，实际后两种囊括第一种。注意都是考虑，未必抢
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # 考虑抢首不抢尾
        pre_max = 0
        cur_max = 0
        for num in nums[:-1]:  # py切片左闭右开
            temp = cur_max
            cur_max = max(cur_max + num, pre_max)
            pre_max = temp
        res1 = cur_max

        # 考虑抢尾不抢首
        pre_max = 0
        cur_max = 0
        for num in nums[1:]:
            temp = cur_max
            cur_max = max(cur_max + num, pre_max)
            pre_max = temp
        res2 = cur_max
        return max(res1, res2)

    def rob3(self, root: Treenode) -> int:
        # 3.打家劫舍三：相邻不可且树形dp
        # 必须后序，dp数组是一个长度为2的数组
        dp = self.traversal(root)
        return max(dp)
    
    def traversal(self, node):
        # 下标为0记录不偷该节点所得到的的最大金钱，下标为1记录偷该节点所得到的的最大金钱
        if not node:  # 递归终止条件
            return (0, 0)  # 元组
        
        left = self.traversal(node.left)
        right = self.traversal(node.right)

        # 不偷当前节点，考虑偷子节点（未必偷，选一个最大的）
        val_0 = max(left[0], left[1]) + max(right[0], right[1])

        # 偷当前节点，不偷子节点
        val_1 = node.val + left[0] + right[0]

        return (val_0, val_1)