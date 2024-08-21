# 回溯算法：可控地暴力搜索所有可能性
# 组合之startindex：一个集合求组合，需要startIndex
# 组合之startindex：多个集合（电话号码题）取组合，各集合间互不影响，不用startIndex
# 去重之used：有重复元素时，使用其必须先sort，used会一起回溯，高效;因为涉及到used[i-1],因此要i>0
# 去重之set（以及字典）：有重复元素时，

from types import list

# 2.组合：给定两个正整数n和k，返回1-n的所有可能的k个数的组合
# self.result应定义为[]而不是[[]]
# apend.path[:],应该使用浅拷贝。result.append(path[:])[:][:][:][:][:][:][:][:][:][:][:][:]
# list没.size，应该使用len()
# 注意最后return的缩进

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.result = []
        self.path = []
        self.backtracking(n, k, 1)
        return self.result


    def backtracking(self, n, k, startindex):
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        for i in range(startindex, n - (k - len(self.path)) + 2):  #  不剪枝为n+1
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()
        return

# 3、4、7.组合总和
# 组合总和三：给定一个范围[1,9]的数组选取k个数，一个目标和target，数组中每个数字在每个组合只能使用一次
# 组合总和：给定一个无重复元素的数组，一个目标和target，数组中数字可以无限制被重复选取
# 组合总合二：给定一个有重复元素的数组，一个目标和target，数组中每个数字在每个组合只能使用一次
class SumSolution():
    # 图方便，三个公用
    def __init__(self):
        self.result = []
        self.path = []

    def three_backtracking(self, target, k, startindex):
        if target < 0:
            return
        if len(self.path) == k:
            if target == 0:  # 如果path长度为k但是该数不为0直接返回
                self.result.append(self.path[:])
            return
        
        for i in range(startindex, 9 - (k - len(self.path)) + 2):
            target -= i
            self.path.append(i)
            self.three_backtracking(target, k, i + 1)
            target += i
            self.path.pop()
        return
    

    def backtracking(self, nums, target, startindex):
        if target < 0:
            return
        if target == 0:
            self.result.append(self.path[:])
            return
        
        for i in range(startindex, len(nums)):
            targrt -= nums[i]
            self.path.append(nums[i])
            self.backtracking(nums, target, i)
            targrt += nums[i]
            self.path.pop()
        return
    
    
    def combinationSum2(self, nums):
        self.used = [False] * len(nums)
    def two_backtracking(self, nums, target, startindex):
        if target < 0:
            return
        if target == 0:
            self.result.append(self.path[:])
            return
        
        for i in range(startindex, len(nums)):
            targrt -= nums[i]
            self.path.append(nums[i])
            self.two_backtracking(nums, target, i)
            targrt += nums[i]
            self.path.pop()
        return
    

# 5.电话号码的字母组合
# 本题想说明，startindex何时使用。
# 本题是求不同集合之间的组合，不需要；而组合、组合总和是求同一个集合中的组合，需要
class numSolution:
    def __init__(self):
        self.letter_map = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz",  # 9
        ]
        self.result = []  # 保存每个s
        self.s = ""  # 收集叶子结点结果


        def letter_backtracking(self, digits, index):
            if index == len(digits):  # 如"23"，则index为2，递归深度为2层
                self.result.append(self.s)  # 字符串是不可变的，之前list用了[:]
                return
            digit = int(digits[index])  # 将传入的字符串"23"转换为整型，digit是一个整数
            letters = self.letter_map[digit]  # 将数字对应转换为字符，此时letter是个字符串
            for i in range(len(letters)):  # 递归宽度为len
                self.s += letters[i]
                self.letter_backtracking(digits, index + 1)
                self.s = self.s[:-1]  # 切片是左闭右开，取到倒数第二个元素

        def letter_combinations(self, digits):
            if len(digits) == 0:
                return self.result
            self.letter_backtracking(digits, 0)
            return self.result