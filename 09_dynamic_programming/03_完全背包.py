# 在01背包一维dp基础上，把内层倒序遍历转换为正序，就是可以使用无限次
# 排列组合顺序有讲究，典型问题都可时候建议先物品后背包，可缩小背包范围
from types import list

class Solution:
    def change2(self, amount: int, coins: list[int]) -> int:
        # 1.零钱兑换二: 组合，物品外背包内
        dp = [0]*(amount + 1)  # 不是len(amount + 1)，int没有len用法
        dp[0] = 1  # 若dp[0]为0则dp一直都是0
        for coin in coins:
            for j in range(coin, amount+1):  # 因为要减，所以从coin开始
                dp[j] += dp[j-coin]
        return dp[-1]
    
    def combination_sum4(self, nums: list[int], target: int) -> int:
        # 2.组合总和四：排列，背包内物品外
        dp = [0]*(target + 1)
        dp[0] = 1
        for j in range(1, target + 1):
            for num in nums:
                if j >= num:  # 要限制的在外面，不可(num, target + 1)此时num还未知只可if
                    dp[j] += dp[j-num]
        return dp[-1]
    
    def climbing_stairs(self, n: int, m: int) -> int:
        # 3.爬楼梯进阶：排列
        dp = [0]*(n+1)
        dp[0] = 1
        for j in range(1, m+1):
            for i in range(1, n+1):
                if j >= i:
                    dp[j] += dp[j-i]
        return dp[-1]
    
    def change(self, coins: list[int], amout: int) -> int:
        # 4.零钱兑换：典型完全背包“最少”，初始化为正无穷
        dp = [float('inf')]*(amout + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amout + 1):
                # 初始化时每个值都有，遍历时coin不是连续正整数，是跳跃正整数，取不到的值跳过更新
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        if dp[amout] == float('inf'):
            return -1
        return dp[-1]
    
    def num_squares(self, n: int) -> int:
        # 5.完全平方数：典型完全背包“最少”
        # 上题的简化版，不用考虑不可能情况，本题有1兜底
        dp = [float('inf')]*(n + 1)
        dp[0] = 0
        # 先物品后背包
        for i in range(1, int(n**0.5)+1):
            for j in range(i*i, n + 1):
                dp[j] = min(dp[j - i*i] + 1, dp[j])
        return dp[-1]
        
    def word_break(self, s: str, wordDict: list[str]) -> bool:
        # 6.单词拆分：典型完全背包
        return