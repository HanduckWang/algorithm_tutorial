from typing import List

# 理解n叉树的宽度n（数的个数）和高度k（单个组合数的个数）
# 3.组合优化



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])  # 直接使用append(path)是不正确安全的，这里创建了浅拷贝
            return None
        for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点


# 4组合总和3
class Ssoltion:
    def combination_sum_3(self, k:int, n:int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 0, 1, [], result)
        return result
    def backtracking(self, target_sum, k, current_sum, start_index, path, result):  # 边写边填充参数（多）
        if current_sum > target_sum:  # 剪枝操作1，如果长度为k但和不为目标值，直接返回
            return
        if len(path) == k:
            if current_sum == target_sum:
                result.append(path[:])  # 整数是不可变对象，浅拷贝和深拷贝没有区别。此处为浅拷贝，直接path会有误
            return
        for i in range(start_index, 9 - (k - len(path)) + 2):  # 剪枝操作2，如k=2，搜索9只剩一个无意义，至多到8
            current_sum += i
            path.append(i)
            self.backtracking(target_sum, k, current_sum, i+1, path, result)
            current_sum -= i
            path.pop()
            

        

# 7.组合总合
# 8.组合总合2
# 5.电话号码的字母组合