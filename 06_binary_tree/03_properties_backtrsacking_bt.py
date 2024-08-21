from collections import deque
from types import list
# 迭代法不适合模拟回溯过程，一般考虑递归就可以


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 13.二叉树的所有路径
    def traversal(self, cur, path, result):
        # 二叉树第一次显式回溯，前序遍历
        path.append(cur.val)  # 中放在了终止条件之前，因为最后一个节点也要加入，先加入再终止
        if not cur.left and not cur.right:  # 左右均为空，到达叶子结点
            sPath = '->'.join(map(str, path))
            result.append(sPath)
            return
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop()  # 回溯
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()
    def binary_tree_paths(self, root) -> list[str]:
        result = []
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
    
    # 16.树左下角的值
    # 最后一行最左边的值，前中后均可因为没有中节处理逻辑，层序也很好
    def find_bottom_left_value(self, root: TreeNode) -> int:
        # 题目说至少一个节点不为空，不用判断root
        self.max_depth = float('-inf')  # 设置为最小的浮点数，定义为实例变量
        self.result = None
        self.traversal(root, 0)
        return self.result

    def traversal(self, node, depth):
        # 终止条件首先要是最后一行（有些叶子结点并不是最后一行），其次要是最左边的值（不一定是左子树）
        if not node.left and not node.right:  # node的左右孩子为空找到叶子结点
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return
        # 前序，保证优先搜索左边
        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1

        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1

    def find_blv_iteration(self, root):
        if root is None:
            return 0
        queue = deque()
        queue.append(root)
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == 0:  # 取每一层最左数值，依次覆盖
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

    # 17.路径总和一，二
    # 前中后均可，因为没有中节点的处理逻辑，化求和为减法
    def traversal_l(self, cur: TreeNode, count: int) -> bool:
        if not cur.left and not cur.right and count == 0:  # 到叶子节点，而且计数为0
            return True
        if not cur.left and not cur.right:  #
            return False
        
        if cur.left:
            count -= cur.left.val
            if self.traversal_l(cur.left, count):  # 递归函数返回bool类型
                return True
            count += cur.right.val
        
        if cur.right:
            count -= cur.right.val
            if self.traversal_l(cur.right, count):
                return True
            count += cur.right.val
        return False
    
    def has_path_sum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        return self.traversal_l(root, sum - root.val)
    
    # 26.二叉树的最近公共祖先
    # 后序遍历
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == q or root == p or root is None:
            return root
        
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        
        # 中
        if  left is not None and right is not None:
            return root
        
        if left is None and right is not None:
            return right
        elif left is not None and right is None:
            return left
        else:
            return None
    
    # 
        