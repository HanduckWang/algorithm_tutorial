# 分割问题

class Solution:
    def partition(self, s: str):
        self.path = []
        self.result = []
        self.par_backtracking(s, 0)
        return
    
    def par_backtracking(self, s, startindex):
        if startindex >= len(s):  # 切割线位置已经≥字符串的长度，已找到
            self.result.append(self.path[:])
            return
        
        for i in range(startindex, len(s)):
            if s[startindex: i + 1] == s[startindex: i + 1][::-1]:
                self.path.append(s[startindex:i+1])
                self.par_backtracking(s, i+1)
                self.path.pop()


class IpSolution:

    def restore_ip(self, s:str):
        self.result = []
        self.path = []
        self.backtracking(s, 0)
        return self.result

    def backtracking(self, s, startindex):
        if len(self.path) > 4:
            return
        if startindex == len(s) and  len(self.path) == 4:
            self.result.append('.'.join(self.path))

        for i in range(startindex, min(startindex + 3, len(s))):  # 在循环中限制，而非依靠valid，减少递归
            if self.is_valid(s, startindex, i):
                sub = s[startindex:i+1]
                self.path.append(sub)
                self.backtracking(s, i+1)
                self.path.pop()
        return
    
    def is_valid(self, s, start, end):
    # 它（每一段）必须是一个数字；它不能以0开头，除非这个数字就是0；它的值必须在0到255之间
        if start > end:
            return False
        if s[start] == '0' and start != end:  # 字符串以0开头且不是单个字符
            return False
        num = int(s[start:end+1])  # 字符串转换为整数
        return 0 <= num <= 255
    