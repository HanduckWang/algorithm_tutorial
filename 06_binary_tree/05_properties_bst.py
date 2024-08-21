from typing import List
"""
二叉搜索树是一个有序树：可以将其看作一个递增的有序数组（中序遍历）

若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
它的左、右子树也分别为二叉搜索树

误区：所有结点的值均小于，而不是子节点小于，二者有很大区别

二叉搜索树题目的两种模式，一是转化为递增数组，二是利用二叉搜索树性质if后递归
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 22.二叉搜索树中的搜索
    # 为何有返回值: 搜索到目标节点就return，这才是找到节点就返回（搜索某一条边），若不加return是遍历整棵树
    # 具体参考二叉树公共祖先
    def search_bst(self, root:TreeNode, val:int) -> TreeNode:
        if not root or root.val == val:
            return root
        
        if root.val > val:
            return self.search_bst(root.left, val)
        
        if root.val < val:
            return self.search_bst(root.right, val)
        
    def search_bst_iteration(self, root:TreeNode, val:int) -> TreeNode:
        while root:
            if val < root.val: 
                root = root.left
            if val > root.val:
                root = root.right
            if val == root.val:
                return root
        return None
        
    # 23.验证二叉搜索树
    # 在中序遍历下，输出的二叉搜索树节点的数值是有序序列，等价转化为判断该序列是否递增
    # 不能单纯的比较左节点小于中间节点，右节点大于中间节点；要比较左子树所有节点<中间节点，右子树所有节点>中间节点
    def is_valid_bst(self, root:TreeNode) -> bool:
        array = []
        self.get_array(root, array)
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                continue
            else:
                return False
        return True

    def get_array(self, root:TreeNode, array: list):
        if not root:
            return
        self.get_array(root.left, array)
        array.append(root.val)
        self.get_array(root.right, array)



    # 24.二叉搜索树的最小绝对差：可双指针
    # 当做有序数组，直接比或引入双指针
    def get_minimum_difference(self, root) -> int:
        array = []
        self.get_array(root, array)
        res = float('inf')
        for i in range(len(array)-1):
           diff = array[i+1] - array[i]
           res = min(res, diff)
        return res
        


    # 25.二叉搜索树中的众数
    # 当成普通二叉树的话，全部遍历使用map统计频率后排序；二叉搜索树的话一定是相邻两个元素作比较
    # 定义一些全局变量
    def __init__(self):  
        self.maxCount = 0
        self.count = 0
        self.pre = None
        self.result = []

    def searchBST(self, cur):
        if cur is None:
            return
        self.searchBST(cur.left)
        # 中
        if self.pre is None:  # 第一个节点
            self.count = 1
        elif self.pre.val == cur.val:  # 与前一个节点数值相同
            self.count += 1
        else:  # 与前一个节点数值不同
            self.count = 1
        self.pre = cur  # 更新上一个节点

        if self.count == self.maxCount:  # 有多个众数
            self.result.append(cur.val)

        if self.count > self.maxCount:  # 更新最大值
            self.maxCount = self.count
            self.result = [cur.val]  # 之前记录的不算，要清空
        
        self.searchBST(cur.right)
        return

    # 33.把二叉搜索树转化为累加树：可双指针
    # 右左中，反中序遍历，顺序累加
    def convert_bst(self, root: TreeNode) -> TreeNode:
        self.pre = 0  # 记录前一个节点的值，初始值为none为0
        self.travel(root)
        return root
    
    def travel(self, cur):
        if not cur:
            return
        self.travel(cur.right)
        cur.val += self.pre
        self.pre = cur.val
        self.travel(cur.left)
    
    # 28.二叉搜索树的最近公共祖先
    def tra(self, cur, p, q):
        if not cur:
            return cur
        if cur.val > p.val and cur.val > q.val:  # 左
            left = self.tre(cur.left, p, q)
            if left:
                return left

        if cur.val < p.val and cur.val < q.val:
            right = self.tra(cur.right, p, q)
            if right:
                return right

        return cur
     
    def lowest_common_ancestor(self, root, p, q):
        return self.tra(root, p, q)