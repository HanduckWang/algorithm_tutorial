# 开心数，本题关键：如果某次求和结果之前出现了（所以需要记录并查询就需要哈希），则说明陷入死循环，永远不会归1，需要return false
class Solution:
    def is_happy(self, n: int):
        seen = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in seen:
                return False
            seen.add(n)
        return True