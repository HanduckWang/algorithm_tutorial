from types import list
# 所有都是买之前必须卖。买卖多次不限制次数（冷冻期，手续费）、最多买卖k次
class solution:
    def max_profit1(self, prices: list[int]) -> int:
        # 1.买卖股票最佳时机：只能买卖1次
        length = len(prices)
        if length == 0:
            return 0
        dp = [[0]*2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], -prices[i])  # 第i天持有股票所得最多现金 
            dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i-1][0])  # 第i天不持有股票所得最多现金
        return dp[-1][1]
    
    def max_profit2(self, prices: list[int]) -> int:
        # 2.买卖股票最佳时机二：买卖多次
        length  = len(prices)
        if length == 0:
            return 0
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices)
        return dp[-1][1]

    def max_profit3(self, prices: list[int]) -> int:
        # 3.买卖股票最佳时机三：最多买卖2次
        # dp[i][j][k]：第i天，第j次买卖(0,1次)，k为0（持有状态）1（未持有状态）
        length = len(prices)
        dp = [[[0] * 2 for _ in range(2)] for _ in range(length)]
        dp[0][0][0] = -prices[0]
        dp[0][0][1] = 0
        dp[0][1][0] = -prices[0]
        dp[0][1][1] = 0
        for i in range(1, length):
            dp[i][0][0] = max(dp[i - 1][0][0], dp[i - 1][0][1] - prices[i])
            dp[i][0][1] = max(dp[i - 1][0][1], dp[i - 1][0][0] + prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][1] - prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][1][0] + prices[i])

        return max(dp[-1][1][1], dp[-1][0][1])
    
    def max_profit4(self, prices: list[int], k: int) -> int:
        # 4.买卖股票最佳时机四：最多买卖k次 ?????????
        length = len(prices)
        dp = [[[0] * 2 for _ in range(k)] for _ in range(length)]
        for j in range(k):
            dp[0][j][0] = -prices[0]
            dp[0][j][1] =  0

        for i in range(1, length):
            for j in range(k):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j-1][1] - prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] + prices[i])
        return max(dp[-1][1][1], dp[-1][0][1])
    
    def max_profit5(self, prices: list[int]) -> int:
        # 5.买卖股票最佳时机含冷冻期：买卖多次卖出冻一天
        return
    
    def max_profit6(self, prices: list[int], fee: int) -> int:
        # 6.买卖股票最佳时机含手续费：买卖多次每次手续费，同二
        length = len(prices)
        if length == 0:
            return 0
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i]  - fee)
        return dp[-1][1]