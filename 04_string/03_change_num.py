# python中字符串不可改
class Solution:
    def change(self, s):
        lst = list(s)
        for i in range(len(lst)):
            if lst[i].isdigit():
                lst[i] = "numer"
        return ''.join(lst)