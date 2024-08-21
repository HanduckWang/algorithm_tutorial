# 判断两个字符串是不是变位词
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        record = []  # 长度26的数组

        for i in s:
            record[ord(i) - ord('a')] += 1  # ord获取ASCII码

        for i in t:
            record[ord(i) - ord('a')] -= 1

        # 全为0，才是变位词
        for i in record:
            if record[i] != 0:
                return False
        return True
