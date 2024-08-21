from types import list
# 动态规划五部曲
# 思考：确定dp数组（dp table）以及下标的含义->确定递推公式->dp数组如何初始化->确定遍历顺序->举例推导dp数组
# 代码：dp table -> 初始化 -> 遍历 -> 递推公式 -> 验证
class Solution:
    # 1.斐波那契
    def fib(self, n: int) -> int:
        # 排除corner case，避免遍历报错
        if n == 0:
            return 0
        
        # 创建dp table
        dp = [0] * (n + 1)  # n+1个而不是n个

        # 初始化
        dp[0] = 0
        dp[1] = 1

        # 由前往后遍历
        for i in range(2, n + 1):  # 注意起始与终止，不要覆盖初始化
            # 确定递推公式
            dp[i] = dp [i-1] + dp [i-2]
        return dp[n]
    


    # 2.爬楼梯
    def climb_stairs(self, n: int) -> int:
        if n == 0:
            return 0
        
        dp = [0] * (n + 1)
        # dp[0]没有意义，直接定义1，2
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    # 思考：考虑爬一次可以爬1-m阶楼梯，转换为完全背包问题


    # 3.最小花费爬楼梯
    def min_cost_climb_stairs(self, cost: list[int]) -> int:
        dp = [0] * (len(cost) + 1)  # 长度要＋1，最后一个索引还是len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return dp[len(cost)]
    
    # 4.不同路径
    def unique_paths(self, m: int, n: int):
        dp = [[0] * n for _ in range(m)]  # 创建一个初始二维dp table
        for i in range(0, m):
            dp[i][0] = 1
        for j in range(0, n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]  # 从0开始的，索引要减1

    # 5.不同路径2
    def unique_paths_with_obstacles(self, obstacle_grid)  -> int:
        m = len(obstacle_grid)  # 取行数
        n = len(obstacle_grid[0])  # 取列数

        # 代码题都要考虑，存在异常情况，如何处理
        if obstacle_grid[0][0] or obstacle_grid[m-1][n-1] == 1:
            return 0
        # dp[i][j] ：表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            if obstacle_grid[i][0] == 1:
                continue
            dp[i][0] = 1
        for j in range(n):
            if obstacle_grid[0][j] == 1:
                continue
            dp[0][j] = 1


        for i in range(m):
            for i in range(n):
                if obstacle_grid[i][j] == 1:
                    continue
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]

    # 6.整数拆分
    def integer_break(self, n: int):
        if n < 2:
            return 0
        # dp[i]：分拆数字i，可以得到的最大乘积为dp[i]
        dp = [0] * (n + 1)  # 列表长度为n+1，因为列表从0开始，要处理dp[n]，就必须有n+1个位置，第n+1个位置就是dp[n]
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i // 2 + 1):  # 注意此两处范围
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]  # 注意返回的是n
    

    # 7.不同的二叉搜索树
    def num_trees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1]*dp[i - j]
        return dp[n]