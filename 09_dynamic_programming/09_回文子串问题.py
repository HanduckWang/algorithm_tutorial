# 回文，从中间向两边
# 子序列相关题，定义dp时，自然就会想题目求什么，就如何定义dp数组
# 但注意第一题dp定义不是 [i,j]内字符串回文子串个数
class Solution:
    # 1.回文子串
    def count_substrings(self, s: str) -> int: 
        dp = [[False]*len(s) for _ in range(len(s))]
        res = 0
        length = len(s)
        # dp[i][j]：[i,j]内字符串是否是回文子串
        for i in range(length - 1, -1, -1):  # 注意此处范围必须是这样
            for j in range(i, length):
                if s[i] == s[j]:
                    # 此处单独拎出来初始化也不可避免
                    if j-i <= 1:  # 此处处理了相邻和同一个的情况，后面j-1不会越界
                        res += 1 
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        res += 1
                        dp[i][j] = True
        return res
    # 补充：最长回文子串
    def longestPalindrome(self, s):
        dp = [[False]*len(s) for _ in range(len(s))]
        length = len(s)
        left = 0
        max_length = 1
        # dp[i][j]：[i,j]内字符串是否是回文子串
        for i in range(length - 1, -1, -1):  # 注意此处范围必须是这样
            for j in range(i, length):
                if s[i] == s[j]:
                    if j-i <= 1:  # 此处处理了相邻和同一个的情况，后面j-1不会越界
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                    if j - i + 1 >= max_length:
                        left = i
                        max_length = j-i+1
        return s[left:(left+max_length)]
    


    # 2.最长回文子序列
    def longest_palindrome_subseq(self, s: str) -> int:
        # dp[i][j]：s在[i, j]内最长回文子序列长度
        length = len(s)
        dp = [[0]*length for _ in range(length)]
        for i in range(length):  # 若例子不是一个字母，注释也无妨
            dp[i][i] = 1
        for i in range(length-1, -1, -1):
            for j in range(i+1, length):  # 必须为i+1,否则后面i=0时j-1越界，前面单独定义了ii
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
    
