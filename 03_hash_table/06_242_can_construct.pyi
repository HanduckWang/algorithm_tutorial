# 检查magazine字符串是否包含足够的字符来构造出ransom_note字符串
class Solution:
    def can_construct(self, randsom_note: str ,magezine: str) -> bool:

        table = {}

        # 存储magazine中每个字符出现的次数
        for i in magezine:
            table[i] = table.get(i, 0) + 1

        for i in randsom_note:
            if i not in table or table[i] == 0:  # 这里等于0的情况是比如说m中有2个s，r中有3个，找到时候m中已经消耗完了，存在但为0
                return False
            table[i] -= 1
        return True
