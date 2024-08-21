"""
1.最后栈里还剩元素则左括号多了；
2.消除过程不匹配则左右不匹配
3.字符串未遍历完栈为空则右括号多了
"""

class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == "(":
                stack.append(")")

            elif item == "{":
                stack.append("}")

            elif item == "[":
                stack.append("]")

            elif not stack or stack[-1] != item:  # 如果为空或者栈顶不等，则报错
                return False
            else:
                stack.pop()  # 用于消除匹配的元素，此时不为空且栈顶与item相等

        return True if not stack else False  # 此处的为空返回true，不为空返回false，是用于情况1