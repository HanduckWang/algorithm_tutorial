# 子集问题也是一种组合问题，满足集合无序性（[1,2],[2,1]相同，取过的元素不会重复取）
# 区别在于，它在每个节点收结果，组合分割只在叶子结点收结果，即递归终止条件不同
class Solution:
    def subsets(self, nums: list):
        self.path = []
        self.result = []
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, startindex):
        self.result.append(self.path[:])

        if startindex >= len(nums):  # 可以不加，for自带
            return
        
        for i in range(startindex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()


class DupSolution:
    def subsets_dup(self, nums: list) -> list:
        self.path = []
        self.result = []
        self.used = [False]*len(nums)
        nums.sort()  # 使用used数组先排序
        self.backtracking_dup(nums, 0)  # 这行应该放在最后
        return self.result
    
    def backtracking_dup(self, nums, startindex):
        self.result.append(self.path[:])

        if startindex >= len(nums):
            return
        
        for i in range(startindex, len(nums)):
            # 这里的i>0很重要，否则只有一个0的用例跑不过
            if i > 0 and nums[i] == nums[i-1] and self.used[i-1] == False:
                continue

            self.path.append(nums[i])
            self.used[i] = True
            self.backtracking_dup(nums, i+1)
            self.used[i] = False
            self.path.pop()


# 递增子序列（子集）
# 本题不可sort，所以不能使用used去重，使用set或者dict（比used更低效）
class SubSolution:
    def find_sub_sequences(self, nums):
        self.path = []
        self.result = []
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, startindex):
        if len(self.path) > 1:
            self.result.append(self.path[:])
        
        used = [0]*201
        for i in range(startindex, len(nums)):
            if used[nums[i] + 100] == 1 or (self.path and nums[i] < self.path[i-1]):
                continue
            used[nums[i] + 100] = 1
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.pop()

        return
            

