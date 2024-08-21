# 删除字符串中的所有相邻重复项
class Solution:
    def remove_duplicates(self, s: str) -> str:
        res = []

        for item in s:
            if res and res[-1] == item:
                res.pop()
            else:
                res.append(item)
        return "".join(res)


class Solution:
    def remove_dulicates(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            res[slow] = res[fast]

            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1

            fast += 1

        return "".join(res[0: slow])

