# 对两个数组操作时候dp的定义退一位更方便初始化、简化逻辑
# 初始化本应该都为1，但双数组由于上面提到的退位，初始化为0
from types import list

class Solution: 
    # 1.最长上升子序列，dp[i]:[0, i]中最长上升子序列长度
    def length_of_lis(self, nums: list[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length
        dp = [1] * length  # dp[0]为1，只有一个数字。每一个i最糟糕也有自己的长度，即1
        for i in range(1, length):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # i固定时遍历j取最大值
        return dp[-1]
    
    # 2.最长上升子数组，dp[i]: 以nums[i]为结尾的最长上升子数组长度
    def length_of_lcis(self, nums: list[int]) -> int:
        length = len(nums)
        if length <= 1:
            return 1
        dp = [1] * length
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return dp[-1]
    
    # 3.最长重复子数组：dp[i][j]:以下标i-1为结尾的A和以下标j-1为结尾的B的最长重复子数组长度
    def find_length(self, nums1: list[int], nums2: list[int]) -> int:
        length1 = len(nums1)
        length2 = len(nums2)
        max_length = 1
        dp = [[0] * (length2 + 1) for i in range(length1 + 1)]  # 前列后行
        for i in range(1, length1 + 1):  # 要+1
            for j in range(1, length2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(max_length, dp[i][j])  # 不断更新，相当于if赋值
        return max_length  # 不可返回dp[-1][-1]，两数组长未必相同，不一定是方阵
    
    # 4.最长公共子序列：dp[i][j]:以下标i-1为结尾的A和以下标j-1为结尾的B的最长公共子序列
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)
        dp = [[0] * (length2 + 1) for i in range(length1 + 1)]  # 前列后行
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[length1][length2]
    
    # 5.不相交的线：等价于最长公共子序列
    def max_uncrossed_lines(self, A: list[int], B: list[int]) -> int:
        length1 = len(A)
        length2 = len(B)
        dp = [[0] * (length2 + 1) for i in range(length1 + 1)]  # 前列后行
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[length1][length2]
    
    # 6.最大子序和：以nums[i]为结尾的最大连续子序和为dp[i]
    def max_subarray(self, nums: list[int]) -> int:
        length = len(nums)
        dp = [0] * length
        for i in range(1, length):
            dp[i] = max(dp[i-1] + nums[i], nums[i])  # 其实max就相当于一个if语句
            res = max(res, dp[i])
        return res  # 有正有负，并非最后一个
    
