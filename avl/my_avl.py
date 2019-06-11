"""
1. 自平衡二分搜索树 AVL
2. 使用平衡因子来度量树的平衡性能,这里 树要满足平衡条件,所有的节点左右两个高度差不能大于1
3. 给所有的节点计算高度,叶子节点的高速为1,非叶子节点的高度是他左右节点(以哪个高度大为准),加1
4. 需要辅助函数来判断树是否是 1. 满足二分搜索的条件(中序遍历是顺序结构) 2. 是否是平衡二叉树(评断平衡因子)
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        # 所有的节点初始化的时候高度都是1
        self.height = 1


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        """
        向节点添加元素
        :param val:
        :return:
        """
        self.root = self._add(self.root, val)

    def _add(self, node, val):
        """
        向节点添加元素
        :param node:
        :param val:
        :return:
        """
        if node is None:
            node = Node(val)
            return node
        if node.val == val:
            return node
        if node.val > val:
            node.left = self._add(node.left, val)
        else:
            node.right = self._add(node.right, val)
        # 每次递归完成后,修改节点的高度
        self.get_height(node)

        balance_factor = self.balance_factor(node)
        if balance_factor > 1:
            #平衡被改变了,左边比右边高,右旋转平衡
            if self.balance_factor(node.left) >= 0:

                """
                     y                 y              z
                    / \               /  \           /   \
                   x   T4   --->     z    T4  -->   x      y
                  / \               / \            / \     / \
                 T1   z            x   T3         T1  T2  T3  T4
                     / \          / \
                    T2  T3       T1  T2
                """


                #这个 LL情况
                #平衡因子的左边的左边大于0,表示是左边的左边的左边的节点导致了
                #他不平衡 那么需要右旋转
                node = self._right_rotate(node)
                #获取到新节点后返回回去,那么他自动会街上
            else:
                #这是 LR情况
                #先对node的左子树左旋转 然后对node有旋转
                node.left = self._left_rotate(node.left)
                node = self._right_rotate(node)


        elif balance_factor < -1:
            if self.balance_factor(node.right) <= 0:
                """
                这是RR情况
                """
                node = self._left_rotate(node)
            else:
                #这个RL
                node.right = self._right_rotate(node.right)
                node = self._left_rotate(node)

        return node

    def _right_rotate(self,y):
        """
                     y                  x
                    / \               /  \
                   x   T4   --->     z     y
                  / \               / \   /  \
                 z  T3             T1 T2 T3   T4
                / \
               T1  T2
        :param node:
        :return:
        """
        x = y.left
        T3 = x.right
        x.right = y
        y.left = T3
        #更新节点的height 只需要 x,y的高度，先更新y,然后x变化,再更新x
        self.get_height(y)
        self.get_height(x)
        return x

    def _left_rotate(self,y):
        """
        :param node:
        :return:
        """
        x = y.right
        T3 = x.left
        x.left = y
        y.right = T3
        #更新节点的height 只需要 x,y的高度，先更新y,然后x变化,再更新x
        self.get_height(y)
        self.get_height(x)
        return x


    def check_factor(self):
        # 遍历节点的所有子节点 查看平衡性
        for i in self:
            print(self.balance_factor(i))

    def is_balance(self):
        """
        查看是否是平衡二叉树
        :return:
        """
        for i in self:
            if self.balance_factor(i) > 1:
                return False
        return True

    def is_bst(self):
        """
        查看是否是二叉搜索树
        :return:
        """
        iter = self._is_bst(self.root)
        bst_list = [i for i in iter]
        for j in range(1, len(bst_list)):
            if bst_list[j] < bst_list[j - 1]:
                return False

        return True

    def _is_bst(self, node):
        """
        查看某个节点是否满足二叉搜索
        :param node:
        :return:
        """
        iter = self.middle_iter(node)
        return iter

    def middle_iter(self, node):
        """
        中序遍历
        :param node:
        :return:
        """
        if node.left:
            for i in self.middle_iter(node.left):
                yield i
        yield node.val
        if node.right:
            for i in self.middle_iter(node.right):
                yield i

    def floor_iter(self, node):
        # 层序遍历
        bucket = list()
        bucket.append(node)
        while len(bucket) > 0:
            node = bucket.pop()
            yield node
            if node.left:
                bucket.append(node.left)
            if node.right:
                bucket.append(node.right)

    def __iter__(self):
        return self.floor_iter(self.root)

    def balance_factor(self, node):
        # 计算平衡节点的平衡因子
        if node.left is None and node.right is None:
            return 0
        if node.left is None:
            return 0 - node.right.height
        elif node.right is None:
            return node.left.height
        else:
            return node.left.height - node.right.height

    # 获取树的高度,并且修改树的高度
    def get_height(self, node):
        node.height = self._get_height(node)
        return node.height

    def _get_height(self, node):
        if node.left is None and node.right is None:
            return 1

        if node.left is None:
            return node.right.height + 1
        if node.right is None:
            return node.left.height + 1

        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def find(self, val):
        return self._find(self.root, val)

    def remove(self,val):
        self.root = self._remove(self.root,val)
        return self.root

    def _remove(self,root,val):
        if root == None:
            return None
        if root.val > val:
            root.left= self._remove(root.left,val)
        elif root.val < val:
            root.right= self._remove(root.right,val)
        else:
            root = None
        return root

    def _find(self, node, val):
        if node is None:
            raise IndexError('no value {}'.format(val))
        if node.val == val:
            return node
        if node.val > val:
            return self._find(node.left, val)
        else:
            return self._find(node.right, val)


if __name__ == "__main__":
    t = Tree()
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    t.add(10)
    t.add(5)
    t.add(4)
    t.add(3)
    x = 1
