from operator import add, sub, mul
# 只考虑整数

class Solution:
    # 在类内部定义一个字典，映射操作符到对应的函数
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: x // y }

    def eval_RPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2)) # 第一个出阿里的在运算符后面‘

        return stack.pop()