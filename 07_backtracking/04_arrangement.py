# 排列问题
# 不用使用startIndex了，但需要一used数组，标记已经选择的元素
# used[i-1]用来树层去重（nums俩相同，used为false说明使用过回溯了）
# used[i]判断当前元素是否已选择(树枝上不能重复选自己)，是否进行下一步递归

class Solution:
    def permute(self, nums):
        self.result = []
        self.path = []
        self.used = [False]*len(nums)
        return self.result
    
    def backtracking(self, nums):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        
        for i in range(0, len(nums)):
            if self.used[i] == False:
                self.used[i] = True
                self.path.append(nums[i])
                self.backtracking(nums)
                self.path.pop()
                self.used[i] = False
        return
    

class DubSolution:
    def permute_dub(self, nums):
        self.result = []
        self.path = []
        self.used = [False]*len(nums)
        return self.result
        
    def backtracking(self, nums):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        
        for i in range(0, len(nums)):
            if (i > 0 and nums[i] == nums[i - 1] and self.used[i - 1] is False) or self.used[i] is True:
                continue
            self.used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums)
            self.path.pop()
            self.used[i] = False
        return