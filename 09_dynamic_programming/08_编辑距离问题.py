class Solution:
    # 1.判断子序列，此题t长
    # dp[i][j]以i-1为结尾的字符串s和以j-1为结尾字符串t相同子序列长度
    def is_subsequence(self, s:str, t:str) -> bool:
        dp = [[0]*(len(t)+1) for _ in (len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:  # 注意这里的if是i-1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]  # 删掉t中一个不相等字符
        return dp[-1][-1]
    
    # 2.不同的子序列，此题s长
    # dp[i][j]以i-1为结尾的s出现在以j-1为结尾的t的个数
    def num_distinct(self, s:str, t:str) -> int:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]  # 用或者不用s
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
    
    # 3.两个字符串的删除操作
    # dp[i][j]以i-1为结尾的word1和以j-1为结尾的word2相等要删除最小次数
    def min_distance(self, word1:str, word2:str) -> int:
        dp = [[0]*(len(word2) + 1) for _ in range((len(word1) + 1))]
        for i in range((len(word1) + 1)):
            dp[i][0] = i
        for j in range((len(word2) + 1)):
            dp[0][j] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
        return dp[-1][-1]
    
    # 4.编辑距离
    # dp[i][j]以下标i-1为结尾的w1和以j-1为结尾的w2最近编辑距离
    def min_distance_pro(self, word1:str, word2:str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range((len(word1) + 1))]  # 注意行列，此处和循环是反的
        for i in range((len(word1) + 1)):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        return dp[-1][-1]