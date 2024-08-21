from collections import deque
# 二叉树的属性优先考虑后序，二叉树的构造修改优先考虑前序

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 8.对称二叉树，只能使用后序遍历子树一旦不行就不行
    def is_symmetic(self, root:TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):

        if left == None and right != None: return False
        if left != None and right == None: return False
        if left == None and right == None: return True
        if left.val != right.val: return False

        outside = self.compare(left.left, right.right)  # 写到这里发现需要传入参数，要用两个函数
        inside = self.compare(left.right, right.left)
        return outside and inside
# 需要两个函数有时候是为了力扣需要，需要传入两个参数，但主函数只给了root
 

    # 11.完全二叉树的节点个数
    def count_nodes_level(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # queue = deque() 后 queue.append(root) 和 queue = deque([root]) 这两种功能上等价，deque接受一可迭代参数
        queue = deque([root])
        node_num = 0

        while queue:
            size = len(queue)

            for _ in size:
                node = queue.popleft()
                num += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return node_num
    
    def count_nodes_recursion(self, root: TreeNode) -> int:
          # post_order
          if not root:
              return 0
          

          # 递归调用时候注意self
          num_left = self.count_nodes_recursion(root.left)
          num_right = self.count_nodes_recursion(root.right)
          node_num = 1 + num_left + num_right

          return node_num
    
    def count_nodes_complete(self, root: TreeNode) -> int:
        return

    # 12.平衡二叉树
    def is_balance(self, root: TreeNode) -> bool:
        # 求左右子树高度差是否<=1，求高度使用post order，这个题要使用两个函数，否则返回值容易出问题
        return self.get_height(root) != -1
    def get_height(self, node) -> int:
        if not node:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        # 比较相等使用==
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        height = 1 + max(left_height, right_height)
        
        return height 
    

    # 15.左叶子之和，前中后都可
    def sum_of_left_leaves(self, root: TreeNode) -> int:
        if not root: 
            return 0
        left_value = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            left_value += root.left.val
        left_value += self.sum_of_left_leaves(root.left)  # 注意接收返回值
        left_value += self.sum_of_left_leaves(root.right)
        return left_value
        # 精简 return left_value + self.sum_of_left_leaves(root.left) + self.sum_of_left_leaves(root.right)


    
