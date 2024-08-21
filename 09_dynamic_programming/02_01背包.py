# n件物品、一最多能装w背包；第i件物品的重量是w[i]，价值是v[i]
# 每件物品只能用一次，求解将哪些物品装入背包里物品价值总和max
# 使用一维dp数组，物品遍历的在，背包在内，且内for循环倒序
from types import list
class Solution:
    # 1.分割等和子集（2个）、划分为k个相等的子集、火柴拼正方形（4个）
    # 每个元素的数值即是重量也是价值
    def can_partition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        dp = [0]*(target + 1)

        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = max(dp[j], dp[j-num] + num)
        return dp[-1] == target
    
    # 2.最后一块石头的重量二
    # 尽量让石头分成两堆相同重量。与1同
    # 最后对dp[target]的处理不同，本题求背包最多能装多少，上题求是否正好装满
    def last_stone_weight(self, stones: list[int]) -> bool:
        total_sum = sum(stones)
        target = total_sum//2
        dp = [0] * (target + 1)

        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j] = max(dp[j], dp[j-stone] + stone)
        return total_sum - 2 * dp[-1]  # 注意此处不是target - dp[-1]
    
    # 3.目标和
    # 在集合nums中找出和为x（加法总和）的组合，可回溯（组合总和）但超时
    # 递推公式不同，初始化不同。12是求容量j背包，最多能装多少。3是装满容量为x的背包有几种方法。组合问题
    # 求组合排列问题的递推公式，都是类似这种dp[j] += dp[j - nums[i]]
    # dp[j]：填满j（包括j）这么大容积的包，有dp[j]种方法
    def find_target_sum_way(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        if (target + total_sum) % 2 != 0 or target > total_sum:
            return 0
        target_sum = (target + total_sum) / 2

        dp = [0] * len(target_sum + 1)
        dp[0] = 1  # 如果为0都为0
        for num in nums:
            for j in range(target_sum, num-1, -1):  # num-1是一种优化，当你背包比num还小，就装不下了
                dp[j] += dp[j-num]
        return dp[-1]  # dp[target_sum]
    
    # 4.一和零
    # 两个维度的01背包
    # dp[i][j]：最多有i个0和j个1的strs的最大子集大小为dp[i][j]
    def find_max_form(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            ones = s.count('1')
            zeros = s.count('0')
            for i in range(m, zeros -1 ,-1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[-1][-1]  # dp[m][n]